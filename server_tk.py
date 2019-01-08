import socket
import threading
#import time

#поток
class ClientThread(threading.Thread):
    # инициализация
    def __init__(self, client_ip, client_port):
        threading.Thread.__init__(self)
        self.client_ip = client_ip
        self.client_port = client_port
        print(bytes("New server socket thread started for {}: {}".format(self.client_ip, self.client_port), "utf-8"))

	#запуск потока: получаем сообщения и отправляем
    def run(self):
        self.client_ip.send(bytes("Type your name and press enter", "utf-8"))
        self.name = client_ip.recv(size).decode("utf-8")
        self.client_ip.send(bytes("Welcome {} to chat".format(self.name), "utf-8"))
        message = "{} has joined to chat"
        self.broadcast(bytes(message.format(self.name), "utf-8"))
        clients[self.client_ip] = self.name
        while True:
			#если сообщение exit, то выходим, иначе отправяляем сообщения
            try:
                data = self.client_ip.recv(size).decode("UTF-8")
                # получим время сообщения
                #time_of_message = time.strftime("%Y-%m-%d %H:%M:%S")
                if data == "exit":
                    self.client_ip.send(bytes("Buy {}!".format(self.name), "utf-8"))
                    self.client_ip.close()
                    del clients[self.client_ip]
                    message = "{} has left the chat."
                    self.broadcast(bytes(message.format(self.name), "utf-8"))
                    break
                else:
                    self.broadcast(data, self.name + ": ")
            except:
                pass
    #функция для отправки
    def broadcast(self, message, prefix=""):
        for sock_client in clients:
            sock_client.send(bytes("{} {}".format(prefix, message), "utf-8"))

#список клиентов
clients = {}

#адрес сервера
ip = 'localhost'
port = 9090
size = 1024
connection = 5
#создадим сокет
with socket.socket() as sock:
    sock.bind((ip, port))
    threads = []

    while True:
        sock.listen(connection)
        client_ip, client_port = sock.accept()
        newthread = ClientThread(client_ip, client_port)
        newthread.start()
        threads.append(newthread)
		
    for t in threads:
        t.join()
