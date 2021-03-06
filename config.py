import socket

def config():
    PORT = int(input("Choose the PORT: "))
    SERVER = socket.gethostbyname(socket.gethostname()) #Set the host, in this case we are using local host
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    SEPARATOR = '<SEPARATOR>'
    BUFFER_SIZE = 200000 #Set the maximum size file to receive in bytes

    return PORT, SERVER, ADDR, FORMAT, SEPARATOR, BUFFER_SIZE
