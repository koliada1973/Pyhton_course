import socket, random
from threading import Thread
from datetime import datetime
# from colorama import init, Fore

# init colors
# init()

# set the available colors
# colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
#           Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
#           Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
#           Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
#           ]

# choose a random color for the client
# client_color = random.choice(colors)


SERVER_HOST = 'localhost'
SERVER_PORT = 5678

s= socket.socket()
# Прописати параметри з'єднання ?
print(f'Connecting on {SERVER_HOST}:{SERVER_PORT}')
s.connect((SERVER_HOST, SERVER_PORT))
print(f'Connected')

name = input('Enter your name:')

def listen_for_message():  # звернути увагу, що реалізовуємо в додатковому треді
    while True:
        message = s.recv(1024).decode()
        print(message)

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
    if send.split()[0] in ['/list', '/create', '/join', '/rename', '/exit']:
        s.send(send.encode())
    elif send.split()[0] == '/close':
        s.close()
        break
    else:
        date_str = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # to_send = f'{client_color}[{date_str}] {name}: {send} {Fore.RESET}'
        to_send = f'[{date_str}] {name}: {send}'
        s.send(to_send.encode())

#     # send = input('[*]: ')
#     send = input()
#     if send.split()[0] == '/list':
#         break
#     date_str = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#     # to_send = f'{client_color}[{date_str}] {name}: {send} {Fore.RESET}'
#     to_send = f'[{date_str}] {name}: {send} '
#     s.send(to_send.encode())
#
# s.close()








