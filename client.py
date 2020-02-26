import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print(hostname, IP)

MAX_CONNECTIONS = 1
address_to_server = ("192.168.56.1", 8686)

clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]
for client in clients:
    client.connect(address_to_server)

command = input("Enter your command: ")

for i in range(MAX_CONNECTIONS):
    clients[i].send(bytes(command, encoding='UTF-8'))

for client in clients:
    message = client.recv(1024)