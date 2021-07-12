import socket

def config():
    HEADER = 64
    PORT = int(input("Choose the PORT: "))
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    SEPARATOR = '<SEPARATOR>'
    BUFFER_SIZE = 200000 #send 4094 bytes each time step

    return HEADER, PORT, SERVER, ADDR, FORMAT, SEPARATOR, BUFFER_SIZE