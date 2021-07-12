import socket
import threading
import config
import os
import datetime
import time

HEADER, PORT, SERVER, ADDR, FORMAT, SEPARATOR, BUFFER_SIZE = config.config()

TIMEOUT = int(input("Set a max timeout in seconds: "))

print(f'PORT: {PORT}\nSERVER: {SERVER}')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def timestamp(filename, filetype):
    date = str(datetime.datetime.now()).split('.')[0]
    filename = filename + "_" + date +"."+ filetype
    filename = filename.replace(" ", "")
    filename = filename.replace(":", "")
    filename = filename.replace("-", "")

    return filename

def save_file(bytes_read, filename, filetype, conn):
    connected = True
    max_value = 0
    filename = timestamp(filename.split("_")[0], filetype)
    with open(filename, 'wb') as f:
        while connected:
            f.write(bytes_read)
            bytes_read = conn.recv(BUFFER_SIZE)
            max_value += len(bytes_read)
            if not bytes_read:
                connected = False
                print(f"File received: {filename}\n[ENDING CONNECTION]")
            elif max_value <= BUFFER_SIZE:
                f.close()
                time.sleep(1)
                save_file(bytes_read, filename, filetype, conn)


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    try:
        conn.settimeout(TIMEOUT)
        max_value = 0
        received = conn.recv(BUFFER_SIZE).decode(FORMAT)
        conn.settimeout(None)
        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        filename, filetype = filename.split('.')
        filename = timestamp(filename, filetype)
        filesize = int(filesize)

        with open(f"{filename}", 'wb') as f:
            while True:
                bytes_read = conn.recv(BUFFER_SIZE)
                max_value += len(bytes_read)
                if not bytes_read:
                    print(f"File received: {filename}\n[ENDING CONNECTION]")
                    break
                elif max_value > BUFFER_SIZE:
                    f.close()
                    time.sleep(1)
                    save_file(bytes_read, filename, filetype, conn)
                else:
                    f.write(bytes_read)
            conn.close()
    except:
        print(f"Error: TimeOut\n[DISCONNECTED] {addr}")
        conn.close()

def start_conn():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    connected = True
    while connected:
        try:
            conn, addr = server.accept()
            # ALLOWS MULTIPLE CLIENTS   
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')
        except:
            print(f"Error: TimeOut")

print("[STARTING] server is starting...")
start_conn()
