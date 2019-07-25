import socket
from threading import Thread
import subprocess
import os

class ClientThread(Thread):

        def __init__(self,client,ip,port):
                Thread.__init__(self)
                self.conn = client
                self.ip = ip
                self.port = port
                print("New server socket thread started for " + ip +":"+str(port))

        def run(self):
                while True:
                        data = self.conn.recv(2048)
                        print("Server received data:",data)
                        MESSAGE = subprocess.check_output(['arp','-a',data])
                        self.conn.send(MESSAGE)
                        break
TCP_IP = '0.0.0.0'
TCP_PORT = 5060
BUFFER_SIZE = 20


tcpServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP,TCP_PORT))
threads = []

while True:
        tcpServer.listen(5)
        print("Waiting for connection:")
        (client,(ip,port)) = tcpServer.accept()
        newThread = ClientThread(client,ip,port)
        newThread.start()
        threads.append(newThread)

for t in threads:
        t.join()
