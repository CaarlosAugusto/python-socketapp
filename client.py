import socket
import config
import os
import tqdm

PORT, SERVER, ADDR, FORMAT, SEPARATOR, BUFFER_SIZE = config.config()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"[CONNECTED] SERVER: {SERVER}")

filename = input("Type the filename to send: ")
filesize = os.path.getsize(filename)

def send(filename, filesize):    
    client.send(f'{filename}{SEPARATOR}{filesize}'.encode(FORMAT))
    
    progress = tqdm.tqdm(range(filesize), f'Sending {filename}', unit='B', unit_scale=True, unit_divisor=1024)
    with open(filename, 'rb') as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            client.sendall(bytes_read)
            progress.update(len(bytes_read))
    client.close()


send(filename, filesize)
