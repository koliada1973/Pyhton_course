import socket
from threading import Thread
from datetime import datetime

SERVER_HOST = 'localhost'
SERVER_PORT = 5678

s = socket.socket()

print(f'Connecting on {SERVER_HOST}:{SERVER_PORT}')
s.connect((SERVER_HOST, SERVER_PORT))
print(f'Connected')

name = input('Enter your name: ')


def listen_for_message():
    while True:
        try:
            message = s.recv(1024).decode()
            if not message:
                print("Server closed connection.")
                break
            print(message)
        except:
            break


task = Thread(target=listen_for_message, daemon=True)
task.start()

commands = """ All available commands
/list : Get all rooms
/create room_name password : Create new room
/join  room_name password : Join to existing room
/rename room_name new_room_name : Rename room by administrator
/exit : Exit from current room
/close : Close program  
"""
print(commands)

while True:
    send = input()
    if not send.strip():
        continue  # ігноруємо пустий ввод

    parts = send.split()
    cmd = parts[0]

    if cmd in ['/list', '/create', '/join', '/rename', '/exit']:
        s.send(send.encode())

    elif cmd == '/close':
        s.send('/exit'.encode())  # повідомляємо сервер
        s.close()
        break

    else:
        date_str = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        to_send = f'[{date_str}] {name}: {send}'
        s.send(to_send.encode())