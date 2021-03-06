# python-socketapp
This software receives data from the network and saves this data to files locally, It will be a server that will receive data via stream (socket) and will save the data to files up to X bytes.

## Requirements:
* Python 3

## How to run:
```
$ pip install -r requirements.txt
```
* To run the server put in a prompt command:
```
$ python server.py
```
* To run the client put in other prompt command:
```
$ python client.py
```
* In both prompts, put the same PORT to connect SERVER and CLIENT like the example below:
```
$ Choose the PORT: 5050
```
* To send a file from client, enter with the path/filename when requested:
```
$ Type the filename to send: client_files/filename.xlsx
```
## Configuring the server:
* Open the config.py file to set the maximum file size to receive in the BUFFER_SIZE variable.
* 'Port' and 'TimeOut' is defined when you inicialize the server.

## Libraries used in this project:
Note: Only the 'tqdm' library need to be install
* socket: to create a socket and connect the client to the server
* threading: to run mulitple clients in the server
* datetime: to set a timestamp
* time: to wait time if necessary
* tqdm: progress bar

## Time spent to create:
About 4 hours for 3 days.
Total: 16 hours

## Difficulties faced in the challenge:
* Learn how sockets works.
* Split files if data is bigger than maximum size configured.
* Set a timeout to cancel the connection if the client doesn't trasmit data for a period of time.
