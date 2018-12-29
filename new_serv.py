import socket 
import threading
import time

class ClientThread(threading.Thread): 
    #инициализация
    def __init__(self,ip,port): 
        threading.Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print("New server socket thread started for {}: {}".format(self.ip, self.port))

    def run(self): 
        while True : 
            try:
                data = self.ip.recv(size)
                # получим время сообщения
                time_of_message = time.strftime("%Y-%m-%d %H:%M:%S")
                # декодируем сообщение
                updata = data.decode("UTF-8")
                # показать сообщения, которые были добавлены в память
                if updata == "all messages":
                    result = list(class_memory.return_list())
                    print("{}".format(result))
                    self.ip.send(bytes("{}".format(result), "UTF-8"))
                # закрываем подключение
                elif updata == "exit":
                    self.ip.send(b"Buy!")
                    self.ip.close()
                    print("Client {} unlinked".format(self.ip))
                # добавляем сообщение и время в память
                else:
                    class_memory.add(time_of_message, updata)
                    print("We added {} and '{}' at the memory".format(time_of_message, updata))
            except:
                pass
                

class Memory:
    """
    память сервера
    """
    def add(self, data, message):
        self.data = data
        self.message = message
        memory[self.data] = self.message
        return memory
    def return_list(self):
        for key in memory:
            yield(key, memory[key])

memory = {}
class_memory = Memory()

ip = 'localhost' 
port = 9090 
size = 1024
with socket.socket() as sock:
    sock.bind((ip, port)) 
    threads = [] 
 
    while True: 
        sock.listen(4) 
        print("Waiting for connections from clients...")
        ip, port = sock.accept() 
        newthread = ClientThread(ip,port) 
        newthread.start() 
        threads.append(newthread) 
 
    for t in threads: 
        t.join() 
