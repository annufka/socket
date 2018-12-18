# -*- coding: utf-8 -*-
import socket

def fib(max):
        try:
                int(float(max))
        except:
                pass
        else:
                a, b = 0, 1
                while a < int(float(max)):
                        yield a
                        a, b = b, a+b

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print('connected: ', addr)
while True:
    data = conn.recv(1024)
    updata = data.decode("utf-8")
    result = list(fib(updata)) 
    conn.send(bytes('{}'.format(result), 'UTF-8'))
    sock.close()


