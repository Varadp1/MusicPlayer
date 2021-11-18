import tkinter as tk
from tkinter.filedialog import askopenfilename
import audioplayer

def open_song():
    global player
    global song_path
    song_path = askopenfilename(initialdir="D:/", title="Please select a music file",
                                filetypes=(("Mp3 Files", "*.mp3"), ("Wav Files", "*.wav"),
                                           ("Ogg files", "*.ogg")))

    if song_path != "":
        with open("Path.txt", "w") as f:
            f.write(song_path)
        label_manage(label,song_path)
        player.stop()
        play_pause_btn.config(text="Play",command=lambda : play(song_path))
    else:
        with open("Path.txt", "r") as f:
            song_path = f.read()

        player.stop()
        play_pause_btn.config(text="Play",command=lambda : play(song_path))


def label_manage(label, text):
    label.config(text=text)


def play(path):
    global label
    global player
    global play_pause_btn

    if path != "":
        player = audioplayer.AudioPlayer(path)
        player.volume = volume
        player.play()
        play_pause_btn.config(text="Pause",command=lambda : pause(player))    
    else:
        label_manage(label, "Please select a song!")


def pause(player):
    player.pause()
    play_pause_btn.config(text="Resume",command=lambda : resume(player))


def resume(player):
    player.resume()
    play_pause_btn.config(text="Pause",command=lambda : pause(player))


def stop(player):
    global play_pause_btn

    play_pause_btn.config(text="Play",command=lambda : play(song_path))
    player.stop()

def volume(volumee):
    global volume
    global player
    global volume_control

    volume = volume_control.get()
    player.volume = volume


root = tk.Tk()

root.title("Music Player")

root.geometry("480x250")

label = tk.Label(relief="ridge", width=500, height=3, border=5,
                 font="Franklin 11")
label.pack()

chng_btn = tk.Button(text="Change Song", width=15, height=3,
                     command=open_song, font="Franklin 13 bold")
chng_btn.place(x=0, y=70)

play_pause_btn = tk.Button(text="Play", width=15, height=3,
                     command=lambda: play(song_path), font="Franklin 13 bold")
play_pause_btn.place(x=160, y=70)

stop_btn = tk.Button(text="Stop", width=15, height=3,
                     command=lambda: stop(player), font="Franklin 13 bold")
stop_btn.place(x=320,y=70)

volume_control = tk.Scale(root,from_=0, to=100, orient="horizontal", command=volume, length=300)
volume_control.set(100)
volume_control.place(x=90,y=160)
volume_label = tk.Label(root, text="Volume")
volume_label.place(x=210,y=200)

with open("Path.txt") as f:
    song_path = f.read()

    if song_path != "":
        label_manage(label,song_path)
    else:
        label_manage(label,"No song found. Please click the change song button and select your song.")

    player = audioplayer.AudioPlayer(song_path)
root.mainloop()