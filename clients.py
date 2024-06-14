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

        def goahead(self,name):
            self.login.destroy()
            self.name=name
            rcv=Thread(target=self.recieve)
            rcv.start()
            
        def recieve(self):
            while True:
                try:
                    message=client.recv(2048).decode('utf-8')
                    if message=='NICKNAME':
                        client.send(self.name.encode('utf-8'))
                    else:
                        print(message)
                except:
                    print('error occured')
                    client.close()
                    break

g=GUI()

def write():
    while True:
        message='{}:{}'.format(nickname,input(''))
        client.send(message.encode('utf-8'))


recieve_thread=Thread(target=recieve)
recieve.start()
write_thread=Thread(target=write)
write_thread.start()
