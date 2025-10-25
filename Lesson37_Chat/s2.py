import socket
from threading import Thread

SERVER_HOST = 'localhost'
SERVER_PORT = 5678

# база клієнтів: {conn: [роль, кімната]}
client_database = {}
# список кімнат: {name:password}
rooms = {}

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)

print(f'Listening on {SERVER_HOST}:{SERVER_PORT}')


def listen_for_message(con):
    print('Server listening...')
    while True:
        try:
            message = con.recv(1024).decode()
            if not message:
                break  # клієнт закрив з'єднання

            # Команди починаються зі слеша
            if message.startswith('/'):
                parts = message.split()
                command = parts[0]

                # формат: /cmd room password
                if len(parts) == 3:
                    _, current_room_name, password = parts
                elif len(parts) == 2:
                    _, current_room_name = parts
                    password = None
                else:
                    # якщо просто команда без аргументів
                    current_room_name = client_database[con][1]
                    password = None

                if command == '/list':
                    con.send(str(list(rooms.keys())).encode())

                elif command == '/create':
                    rooms[current_room_name] = password
                    client_database[con] = ['admin', current_room_name]
                    con.send(f'Room {current_room_name} created. Reconnect.'.encode())

                elif command == '/join':
                    if rooms.get(current_room_name) == password:
                        client_database[con] = ['user', current_room_name]
                        con.send(f'You joined {current_room_name}'.encode())
                    else:
                        con.send('Wrong name or password'.encode())

                elif command == '/rename':
                    role, room = client_database[con]
                    if role == 'admin' and room == current_room_name:
                        rooms[password] = rooms[current_room_name]
                        del rooms[current_room_name]
                        client_database[con][1] = password
                        con.send(f'{current_room_name} renamed to {password}'.encode())
                    else:
                        con.send("You are not admin".encode())

                elif command == '/exit':
                    role, room = client_database[con]
                    con.send(f'Logout from {room}'.encode())
                    del client_database[con]
                    con.close()
                    break

                else:
                    con.send("Unknown command".encode())

            else:
                # звичайне повідомлення → всім у кімнаті
                current_room_name = client_database[con][1]
                room_clients = {
                    client: data for client, data in client_database.items()
                    if data[1] == current_room_name
                }
                for client in room_clients:
                    try:
                        client.send(message.encode())
                    except:
                        # якщо клієнт відвалився
                        client.close()
                        del client_database[client]

        except Exception as exp:
            print(f'Fail to receive: {exp}')
            if con in client_database:
                del client_database[con]
            con.close()
            break


while True:
    connection, client_address = s.accept()
    print(f'{client_address} connected')

    client_database[connection] = ['sys', 'default']
    task = Thread(target=listen_for_message, args=(connection,), daemon=True)
    task.start()



