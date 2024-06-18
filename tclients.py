import socket
from threading import Thread
from tkinter import *
import random

canvas1=None
player_name=None
name_entry=None
name_window=None
screen_width=None
screen_height=None

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS


    IP_ADDRESS='127.0.0.1'
    PORT=6000

    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    thread=Thread(target=receivedMsg)
    thread.start()

def ask_player_name():
    global player_name
    global name_entry
    global name_window
    global canvas1
    global screen_height
    global screen_width

    name_window=Tk()
    name_window.title('Tambola Family Fun')
    name_window.attributes('-fullscreen',True)
    

    screen_width=name_window.winfo_screenwidth()
    screen_height=name_window.winfo_screenheight()

    bg=ImageTk.PhotoImage(style="./assets/background.png")

    canvas1=Canvas(name_window,width=500,height=500)
    canvas1.pack(fill='both',expand=True)

    canvas1.create_image(0,0,image=bg,anchor='nw')
    canvas1.create_text(screen_width/4.5,screen_height/8,text='Enter Name',font=('Chalkboard SE',60),fill='black')

    name_entry=Entry(name_window,width=15,justify='center',font=('Chalkboard SE',30),bd=5,bg='white')
    name_entry.place(x=screen_width/7,y=screen_height/5.5)

    button=Button(name_window,text='Save',font=('Chalkboard SE',30),width=11,command=savename,height=2,bg='#80deea',bd=3)
    button.place(x=screen_width/6,y=screen_height/4)
   
    name_window.resizable(True,True)
    name_window.mainloop()

def savename():
    global SERVER
    global player_name
    global name_entry
    global name_window

    player_name=name_entry.get()
    name_entry.delete(0,END)
    name_window.destroy()

    SERVER.send(player_name.encode())

setup()