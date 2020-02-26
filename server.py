import socket

SERVER_ADDRESS = ('192.168.56.1', 8686)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(1)
print("Server is running")

while True:
    connection, address = server_socket.accept()

    message = connection.recv(1024)

    if str(message) == "b'sleep'":
        print("i'm sleeped")
    elif str(message) == "b'shutdown'" or str(message) == "b'sd'":
        print("i'm power off")
    else:
        print("Unknown command", str(message))

    connection.send(bytes("OK", encoding='UTF-8'))

    connection.close()