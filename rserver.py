import socket
from threading import Thread
from pynput.mouse import Button,Controller
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller

IP_ADDRESS = '192.168.0.111'
PORT = 8080
SERVER = None
screen_height=None
screen_width=None

keyboard=Controller()

def setup():
    print('Welcome to remote mousse!')

    global SERVER
    global port
    global ip_address

    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((ip_address,port))
    SERVER.listen(10)

    print('Server is waiting for incoming connections...')
    get_device_size()
    acceptConnections()

def acceptConnections():
    global SERVER
     
    while True:
        client_socket,addr=SERVER.accept()
        print(f'connection established with {client_socket}:{addr}')

        thread1=Thread(target=receive_message(),args=(client_socket,))
        thread1.start()

def get_device_size():
    global screen_width
    global screen_height

    for i in get_monitors():
        screen_width=int(str(i).split(',')[2].strip().split('width=')[1])
        screen_height=int(str(i).split(',')[3].strip().split('height=')[1])

def receive_message(client_socket):
    global keyboard
    while True:
        try:
            message=client_socket.recv(2048).decode()
            if message:
                keyboard.press(message)
                keyboard.release(message)
                print(message)

        except Exception as error:
            pass
            