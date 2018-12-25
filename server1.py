import socket
import time
import multiprocessing as mp

#процесс
def one_client(sock):
    conn, addr = sock.accept()
    print("connected: ", addr)
    sock.send(b"OK")
    class_memory = Memory()
    while True:
        data = conn.recv(1024)
        time_of_message = time.strftime("%Y-%m-%d %H:%M")
        updata = data.decode("UTF-8")
        if updata == "all messages":
            result = list(class_memory.return_list())
            print(result)
            conn.send(bytes("{}".format(result), "UTF-8"))
        else:
            class_memory.add(time_of_message, updata)
            print("We added {} and '{}' at the memory".format(time_of_message, updata))


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


with socket.socket() as sock:
    sock.bind(('', 9090))
    sock.listen(5)

    while True:
        clients = workers = [mp.Process(target=one_client, args=(socket,)) for i in range(5)]
        for number_of_process in clients:
            number_of_process.start()
            number_of_process.join()

