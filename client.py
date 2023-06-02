import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():

    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure("LightSkyBlue")

    listbox = Listbox(window, height=10, width= 19, activestyle="dotbox", bg="SkyBlue", font=('calibri', 10))
    listbox.place(x=10, y=10)

    selectLabel = Label(window, text="Select song", bg="LIghtSkyBlue", font=('calibri', 8))
    selectLabel.place(x=2, y=1)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command= listbox.yview)

    playButton = Button(window, text="Play", bd=1, width=10, bg="SkyBlue", font=('calibri', 10))
    playButton.place(x=30, y=200)

    stopButton = Button(window, text="Stop", bd=1, width=10, bg="SkyBlue", font=('calibri', 10))
    stopButton.place(x=200, y=200)

    upload = Button(window, text="Upload", bd=1, width=10, bg="SkyBlue", font=('calibri', 10))
    upload.place(x=30, y=250)

    download = Button(window, text="Download", bd=1, width=10, bg="SkyBlue", font=('calibri', 10))
    download.place(x=200, y=250)

    infoLabel = Label(window, text="", fg="blue", font=("calibri", 8))
    infoLabel.place(x=4, y=200)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()