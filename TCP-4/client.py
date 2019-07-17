import socket

host = socket.gethostname()
port = 5060
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientA: Enter ip:")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE.encode('ascii'))
    data = tcpClientA.recv(BUFFER_SIZE)
    print("Client2 received data:", data)
    break

tcpClientA.close()

