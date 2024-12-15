from tkinter import *
from yt_dlp import YoutubeDL 
import os

if not os.path.exists("downloads"):
    os.makedirs("downloads")


def hq():
    try:
        dq=entry.get()
        downq={
            'format':'best',
            'outtmpl':'downloads/%(title)s.%(ext)s'
        }
        
        with YoutubeDL(downq)as yd:
            yd.download([dq])
            print("video downloaded successfully")
            
    except Exception as x:
        print("ERROR")
        
        
        
def lq():
    try:
        dq=entry.get()
        downq={
            'format':'worst',
            'outtmpl':'downloads/%(title)s.%(ext)s'
        }
        
        with YoutubeDL(downq)as yd:
            yd.download([dq])
            print("video downloaded successfully")
            
    except Exception as x:
        print("ERROR")
        
        
        
def get_audio():
    try:
        dq=entry.get()
        downq={
            'format':'bestaudio',
            'outtmpl':'downloads/%(title)s.%(ext)s'
        }
        
        with YoutubeDL(downq)as yd:
            yd.download([dq])
            print("video downloaded successfully")
            
    except Exception as x:
        print("ERROR")
        
        

window = Tk()
window.title("multi_project")
window.geometry("800x500")
window.configure(bg="#C1CDCD")

Label=Label (window,text="add your youtube link here",font="bold",bg=window['bg'])
Label.place(x=300,y=30)

entry=Entry(window,width=50)
entry.place(x=240,y=75)

high=Button(window,text="high quality",command=hq,font="bold",activebackground="#E0EEEE")
high.place(x=140,y=150)

low=Button(window,text="low quality",command=lq,font="bold",activebackground="#E0EEEE")
low.place(x=350,y=150)

audio=Button(window,text="get audio",command=get_audio,font="bold",activebackground="#E0EEEE")
audio.place(x=560,y=150)


window.mainloop()