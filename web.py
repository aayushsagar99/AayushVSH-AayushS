import socket
my_socket = socket.socket()
my_socket.connect('www.google.com')
my_socket.send("testing, testing")
recived=my_socket.recv()
print(recived) 