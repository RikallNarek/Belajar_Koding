import tkinter as tk
from tkinter import filedialog
import pygame 

# inisialisasi
pygame.mixer.init()

# fungsi pilih lagu
def load_music():
    global song
    song = filedialog.askopenfilename()
    label.config(text=song)

# play
def play_music():
    try:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        status.config(text="▶ Playing")
    except:
        status.config(text="Pilih lagu dulu!")

# pause
def pause_music():
    pygame.mixer.music.pause()
    status.config(text="⏸ Paused")

# resume
def resume_music():
    pygame.mixer.music.unpause()
    status.config(text="▶ Resume")

# stop
def stop_music():
    pygame.mixer.music.stop()
    status.config(text="⏹ Stopped")

# GUI
root = tk.Tk()
root.title("Music Player Sederhana")
root.geometry("300x250")

song = ""

label = tk.Label(root, text="Belum ada lagu", wraplength=250)
label.pack(pady=10)

btn_load = tk.Button(root, text="Pilih Lagu", command=load_music)
btn_load.pack(pady=5)

btn_play = tk.Button(root, text="Play", command=play_music)
btn_play.pack(pady=5)

btn_pause = tk.Button(root, text="Pause", command=pause_music)
btn_pause.pack(pady=5)

btn_resume = tk.Button(root, text="Resume", command=resume_music)
btn_resume.pack(pady=5)

btn_stop = tk.Button(root, text="Stop", command=stop_music)
btn_stop.pack(pady=5)

status = tk.Label(root, text="Status: -")
status.pack(pady=10)

root.mainloop()