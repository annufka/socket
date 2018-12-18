# -*- coding: utf-8 -*-
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(bytes('10', 'UTF-8'))
data = sock.recv(1024)
print(data.decode())
sock.close()
