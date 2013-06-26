from socket import socket, AF_INET, SOCK_STREAM 
import  sys , threading

class Cliente(object):
   
    def __init__(self, port, ip):
        
        self.IP = ip
        self.puerto = port
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((self.IP, self.puerto))
        

    def enviar_mensajes(self):

        while(True):
            mensaje= raw_input()
            self.socket.send(mensaje)

    def recibir_mensaje(self):

        while True:
            msg = self.socket.recv(4096) # recibimos mensajes
            print msg

    def run(self):

        threading.Thread(target= self.enviar_mensajes).start()
        threading.Thread(target= self.recibir_mensaje).start()

