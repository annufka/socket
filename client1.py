# -*- coding: utf-8 -*-
import socket

sock = socket.socket()
sock.connect(("localhost", 9090))
sock.send(bytes("Hello", 'UTF-8'))

sock.send(bytes("smth", 'UTF-8'))
sock.send(bytes("all messages", "UTF-8"))
data = sock.recv(1024)
print(data.decode("UTF-8"))

