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
## Configuring the server:
* Open the config.py file to config set the maximum size file to receive.
* Other configs like 'Port' and 'TimeOut' is defined when you inicialize the server

## Libraries used in this project:
* socket: to create a socket and connect the client to the server
* threading: to run mulitple clients in the server
* datetime: to set a timestamp
* time: to wait time if necessary
* tqdm: progress bar

## Time spent to create:
About 4 hour for 3 days
Total of 12 hours

## Difficulties faced in the challenge:
* Learn how sockets works.
* Split files if data is bigger than maximum size configured.
* Set a timeout to cancel the connection if the client doesn't trasmit data for a period of time.
