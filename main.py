from pytube import YouTube
import time
import tkinter as tk
from tkinter import filedialog
import os
import webbrowser
def urlopen():
    webbrowser.open_new('https://github.com/MarvesCoding/Youtube_Downloader')
user = os.getlogin()
def download(): 
    video = YouTube(inputurl.get())
    stream = video.streams.get_highest_resolution()
    stream.download('C:/Users/'+ user + '/Downloads')
    inputurl.delete("0", tk.END)
    tk.Label(
        text="Saved to Downloads",
        width=19,
        height=1,
    ).place(x=130, y=75)
window = tk.Tk()
window.geometry("400x200")
window.title("Marve's Youtube Downloader")
img = tk.PhotoImage(file="bk.png")
label = tk.Label(
    window,
    image=img
)
label.place(x=-5, y=-5)
inputurl = tk.Entry(
    text="Paste url here: ",
    width=50
)
welcome = tk.Label(
    text = "Paste your video url below",
    foreground='white',
    background="black",
    )
dlbtn = tk.Button(
    text="Download",
    width=10,
    height=1,
    bg="black",
    fg="white",
    command=download
)
exitbtn = tk.Button(
    text="Close",
    width=10,
    height=1,
    bg="black",
    fg="white",
    command=window.destroy
)
helpbtn = tk.Button(
    text="Help",
    width=10,
    height=1,
    bg="black",
    fg="white",
    command=urlopen
)
welcome.place(x=130, y=5)
helpbtn.place(x=300, y=5)
dlbtn.place(x=25, y=155)
exitbtn.place(x=300, y=155)
inputurl.place(x=50, y=100)
window.resizable(False, False)
window.mainloop()