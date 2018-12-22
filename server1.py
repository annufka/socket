import socket
import time

#память сервера
class Memory:
    def __init__(self):
        self.memory = {}
    def add(self, data, message):
        self.data = data
        self.message = message
        self.memory[self.data] = self.message
        return self.memory
    def return_list(self):
        for key in self.memory:
            yield(key, self.memory[key])


clients = {}
sock = socket.socket()
sock.setblocking(0)
sock.bind(('', 9090))
sock.listen(20)

while True:
    conn, addr = sock.accept()
    clients[addr] = conn
    print("connected: ", addr)
    class_memory = Memory()
    while True:
        data = conn.recv(1024)
        """
        if not data: 
            break
        """
        time_of_message = time.strftime("%Y-%m-%d %H:%M")
        updata = data.decode("UTF-8")
        if updata == "all messages":
            result = list(class_memory.return_list())
            print(result)
            conn.send(bytes("{}".format(result), "UTF-8"))
        else:
            class_memory.add(time_of_message, updata)
            print("We added {} and '{}' at the memory".format(time_of_message, updata))

sock.close()
