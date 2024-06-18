import socket
from threading import Thread

SERVER=None
PORT=6000
IP_ADDRESS='127.0.0.1'

def setup():
    print('\n\t\t\t\t\t***Welcome to Tambola Game***\n')

    global SERVER
    global PORT
    global IP_ADDRESS
    
    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen(10)

    print('\t\t\t\tServer is waiting for incoming connections...\n')


def acceptconnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket,addr=SERVER.accept()
        player_name.socket.recv(1024).decode().strip()
        print(player_name)
        if len(CLIENTS.key())==0:
            CLIENTS[player_name]={'player_type':'player 1'}
        else:
            CLIENTS[player_name]={'player_type':'player 2'}

        CLIENTS[player_name]['player_socket']=player_socket
        CLIENTS[player_name]['address']=addr
        CLIENTS[player_name]['player_name']=player_name
        CLIENTS[player_name]['turn']=False

        print(f'Connection established with {player_name} : {addr}')

setup()