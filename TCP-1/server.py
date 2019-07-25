import socket
import subprocess
import os

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('localhost',9998))
socket.listen(1)
client,addr = socket.accept()
i=1
file = 'file'+str(i)+'.c'
i+=1
f = open(file,'wb')
l = client.recv(1024)
f.write(l)
f.close()
subprocess.call(['gcc',file])
exec_file = open('a.out','rb')
read_bytes = exec_file.read(1024)
while(read_bytes):
    client.send(read_bytes)
    read_bytes = exec_file.read(1024)
socket.close()
