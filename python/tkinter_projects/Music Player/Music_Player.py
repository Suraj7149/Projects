from tkinter import *
from tkinter import filedialog
import pygame
root = Tk()
root.title("Music Player.")
root.geometry("800x600")

pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir="G:/Song", title="Choose a Song", filetypes=(("mp3 files","*.mp3"),))
    song = song.replace("G:/Song/", "")
    song = song.replace(".mp3", "")
    song_box.insert(END, song)


def play():
    song = song_box.get(ACTIVE)
    song = f"G:/Song/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


song_box = Listbox(root, bg='#25292e', fg="Blue", width=120, height=25, selectbackground="gray", selectforeground="black")
song_box.pack()

play_button = Button(root, text="Play", command=play)
pause_button = Button(root, text="Pause")
stop_button = Button(root, text="Stop", command=root.destroy)
fwd_button = Button(root, text="Fwd")
bwd_button = Button(root, text="Bwd")

play_button.pack(pady=10)
pause_button.pack(pady=10)
stop_button.pack(pady=10)
fwd_button.pack(pady=10)
bwd_button.pack(pady=10)

my_menu = Menu(root)
root.config(menu=my_menu)

add_songs_menu= Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_songs_menu)
add_songs_menu.add_command(label="Add One Song to playlist", command=add_song)

root.mainloop()
