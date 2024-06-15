import socket
from tkinter import *
from threading import Thread

nickname=input("Choose your nickname: ")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address='127.0.0.1'
port=8000
client.connect((ip_address,port))
print('connected with the server')

class GUI:
    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()

        self.login=Toplevel()
        self.login.title('Login')
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)

        self.pls=Label(self.login,text='please login to continue',justify=CENTER,font='Helvetica 14 bold')
        self.pls.place(relheight=0.15,relx=0.2,rely=0.07)
        self.labelname=Label(self.login,text='Name: ',font='Helvetica 12')
        self.labelname.place(relheight=0.2,relx=0.1,rely=0.2)

        self.entryname=Entry(self.login,font='Helvetica 14')
        self.entryname.place(relheight=0.2,relx=0.35,rely=0.2)
        self.entryname.focus()

        self.go=Button(self.login,text='CONTINUE',font='Helvetica 14 bold',command=lambda: self.goahead(self.entryname.get()))
        self.go.place(relx=0.4,rely=0.55)
        self.Window.mainloop()

        
            
    def recieve(self):
        while True:
            try:
                message=client.recv(2048).decode('utf-8')
                if message=='NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    self.show_msg(message)
            except:
                print('error occured')
                client.close()
                break



    def write():
        send.textcons.config(state=DISABLED)
        while True:
            message=(f'{self.name}: {self.msg}')
            client.send(message.encode('utf-8'))
            self.show_msg(message)
            break
    
    def goahead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.recieve)
        rcv.start()

    def layout(self,name):
        self.name=name
        self.Window.deiconify()
        self.Window.title('CHATROOM')
        self.Window.resizable(width=False,height=False)
        self.Window.configure(width=470,height=550,bg='#17202A')

        self.labelhead=Label(self.Window,bg='#17202A',fg='#EAECEE',text=self.name,font='Helvetica 13 bold',pady=5)
        self.labelhead.place(relwidth=1)

        self.line=Label(self.Window,width=450,bg='#ABB2B9')
        self.line.place(relwidth=1,rely=0.07,relheight=0.012)

        self.textcons=Text(self.Window,width=20,height=2,bg='#17202A',fg='#EAECEE',font='Helvetica 13 bold',pady=5)
        self.textcons.place(relwidth=1,rely=0.08)

        self.labelbottom=Label(self.Window,bg='#ABB2B9')
        self.labelbottom.place(relwidth=1,rely=0.825)

        self.entrymsg=Entry(self.bottom,bg='#2C3E50',fg='#EAECEE',font='Helvetica 13')
        self.entrymsg.place(relwidth=0.74,relheight=0.06,rely=0.008,relx=0.011)
        self.entrymsg.focus()

        self.buttonmsg=Button(self.labelbottom,text='SEND',font='Helvetica 10 bold',width=20,bg='#ABB2B',command=self.sendbutton(self.entrymsg.get()))
        self.buttonmsg.place(relx=0.77,relheight=0.06,relwidth=0.02)

        self.textcons.config(cursor='arrow')
        scrollbar=Scrollbar(self.textcons)
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.config(command=self.textcons.yview)

        self.textcons.config(state=DISABLED)

    def sendbutton(self,message):
        self.textcons.config(state=DISABLED)
        self.msg=message
        self.entrymsg.delete(0,END)
        snd=Thread(target=self.write)
        snd.start()
    
    def show_msg(self,message):
        self.textcons.config(state=NORMAL)
        self.textcons.insert(END,message+'\n\n')
        self.textcons.config(state=DISABLED)
        self.textcons.see(END)

recieve_thread=Thread(target=recieve)
recieve.start()
write_thread=Thread(target=write)
write_thread.start()

g=GUI()



