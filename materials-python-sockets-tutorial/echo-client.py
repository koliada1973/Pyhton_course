import socket

HOST = "127.0.0.1"  # Ім'я хоста або IP-адреса сервера
PORT = 65432  # Порт, який використовується сервером

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Отримано {data!r}")
