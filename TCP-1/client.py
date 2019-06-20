import socket
import os

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost',9998))

pyt_file = open('x.c','rb')
l = pyt_file.read(1024)
while(l):
    client_socket.send(l)
    l = pyt_file.read(1024)
pyt_file.close()
execFile = open('o.out','wb')
amount_read = client_socket.recv(1024)
while(amount_read):
    execFile.write(amount_read)
    amount_read = client_socket.recv(1024)
execFile.close()
os.chmod("o.out",0o777)
client_socket.close()
