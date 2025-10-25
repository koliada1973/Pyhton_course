import socket
from threading import Thread

SERVER_HOST = 'localhost'
SERVER_PORT = 5678

# step 1
# client_sockets = set()
client_database = {} # замість client_sockets; {conn:['admin', 'new_room'], conn:['sys', 'default']}
rooms = {} # {name:password}

s= socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # -- тут уточнити.
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)

print(f'Listening on {SERVER_HOST}:{SERVER_PORT}')

def listen_for_message(con):
    print('Server listening...')
    while True:
        try:
            message = con.recv(1024).decode()
            # step 3
            if len(message.split()) == 3:
                command, current_room_name, password = tuple(message.split())
            else:
                command, current_room_name, password = message, client_database[con][1], None

        except Exception as exp:
            print(f'Fail to recieve with {exp}')
            # continue
            break

        # for client in client_sockets:
        #     client.send(message.encode())
        # step 4
        if command == '/list':
            con.send(str(rooms.keys()).encode())
        elif command == '/create':
            rooms[current_room_name] = password
            client_database[con] = ['admin', current_room_name]
            con.send(f'Reconect to {current_room_name}'.encode())
        elif command == '/join':
            if rooms.get(current_room_name) == password:
                client_database[con] = ['user', current_room_name]
                con.send(f'You are conect to {current_room_name}'.encode())
            else:
                con.send('Wrong name or password'.encode())
        elif command == '/rename':
            # if client_database[con] == {'admin', current_room_name}:
            #     client_database[con][1] = password
            #     con.send(f'{current_room_name} rename to {password}'.encode())
            print(f'client_database: {client_database}')
            print(f'rooms: {rooms}')
            if client_database[con] == ['admin', current_room_name]:
                rooms[password] = rooms[current_room_name]
                del rooms[current_room_name]
                client_database[con][1] = password
                connection.send(f'{current_room_name} rename to {password}'.encode())
            else:
                con.send("You are not admin".encode())
        elif command == '/exit':
            client_database[con] = ['sys', 'default']
            con.send(f'Logout from {current_room_name}'.encode())
        else:
            room_client = dict(filter(lambda x: current_room_name == x[1][1], client_database.items()))
            # for client in client_database:
            for client in room_client:
                client.send(message.encode())


while True:
    connection, client_address = s.accept()
    print(f'{client_address} connected')

    # client_sockets.add(connection)
    # task = Thread(target=listen_for_message, args=(connection,), daemon=True)
    # # task.daemon = True
    # task.start()

    # step 2
    # client_sockets.add(connection)
    client_database[connection] = ['sys', 'default']
    task = Thread(target=listen_for_message, args=(connection,), daemon=True)
    # task.daemon = True
    task.start()




