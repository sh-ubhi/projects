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

def createTicket():
    global game_window 
    global ticket_grid

    mainlabel= Label(game_window,width=65, heigh=16,relief='ridge',borderwidth=5,bg='white')
    mainlabel.place(x=95,y=119)

    xpos=105
    ypos=130
    for row in range(0,3):
        rowlist=[]
        for col in range(0,9):
            if (platform.system()=='Darwin'):
                boxbutton=Button(game_window,font=('Chalkboard SE',18),borderwidth=3,pady=23,padx=22,bg='#fff176',highlightbackground='#fff176',activebackground='@c5ela5')

                boxbutton.place(x=xpos,y=ypos)
            else:
                boxbutton=tk.Button(game_window,font=('Chalkboard SE',30),width=3,heigh=2,borderwidth=5,bg='#fff176')
                boxbutton.place(x=xpos,y=ypos)

            row.appned(boxbutton)
            xpos+=64

    ticket_grid.append(rowlist)
    xpos=105
    ypos+=82

def placeNumbers():
    global ticket_grid
    global current_number_list

    # Here key is index and values are numbers 
    numberContainer={"0": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "1": [10, 11, 12,13, 14, 15, 16, 17, 18, 19],,
    "2": [20, 21, 22, 23,24, 25, 26, 27, 28, 29],
    "3": [30, 31, 32, 33, 34, 35, 36, 37, 38, 39], 
    "4": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 
    "5": [50, 51, 52, 53, 54, 55, 56, 57, 58, 59], 
    "6": [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], 
    "7": [70, 71, 72, 73, 74, 75, 76, 77, 78, 79], 
    "8": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],}
    
    # placing a number to particular position in the ticket 
    counter = 0
    while (counter < len(randomColList)):
        colNum = randomColList[counter]
        numbersListByIndex = numberContainer [str(colNum)] 
        randomNumber = random.choice (numbersListByIndex)

        if (randomNumber not in currentNumberList): 
            numberBox = ticketGrid[row][colNum]
            numberBox.configure (text=randomNumber, fg="black")
            currentNumberList.append(randomNumber)
            
            counter+=1

    for row in range(0,3):
        random_col_list=[]
        counter=0

        while counter<=4:
            random_col=random.randint(0,8)
            if (random_col not in random_col_list):
                random_col_list.append(random_col)
                counter+=1

setup()