from pytube import YouTube
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


ventana=tk.Tk()
ventana.title("Youtube video donwloader")
ventana.grid()
header=ttk.Frame(width=400,height=50)
header.grid(column=0,row=0)
ttk.Label(text="Pegue el URL del video que desea descargar:").grid(column=0,row=2)
url_entry=ttk.Entry()
url_entry.grid(column=0,row=3)
url_entry.insert(0,"URL")

def download ():
    link=str(url_entry.get())
    video=YouTube(link)
    video=video.streams.get_highest_resolution()
    titulo=str(video.title)
    print (titulo)
    try:
        video.download()
    except:
        messagebox.showinfo("Error","Hubo un error al descargar el video, intente de nuevo")
    messagebox.showinfo("Descarga existosa","La descarga del video fue exitosa")

buttom=ttk.Button(text="Descargar video: ", command=download).grid(column=0,row=4)
footer=ttk.Frame(width=400,height=50).grid(column=0,row=5)
ventana.mainloop()