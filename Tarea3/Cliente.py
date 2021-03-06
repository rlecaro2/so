﻿from socket import socket, AF_INET, SOCK_STREAM 
import  sys , threading

class Cliente:
    
    def __init__(self, port, ip):
        
        self.IP = ip
        self.puerto = port
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((self.IP, self.puerto))
        self.ProcesosRecibidos = []
        

    def enviar_mensaje(self, msj):

        ##Formato: enviar_mensaje;Fecha Ejecucion, Tipo Proceso, Prioridad Base,  receptor, texto que se quiere enviar 
        mensaje = msj
        self.socket.send("mensaje;" + mensaje)

    def recibir_mensaje(self):
        while True:
            msg = self.socket.recv(4096) # recibimos mensajes
            print("Instruccion recibida: "+ msg)  
            self.ProcesosRecibidos.append(msg)
    
    def llamar(self):
        pass

    def terminarllamada(self):
        pass

    def finalizarconexion(self):
        self.socket.close()

    def run(self):
       
        threading.Thread(target= self.recibir_mensaje).start()

    def GetIntruccionesRecibidas(self):
        aux = ""
        try:
            aux = self.ProcesosRecibidos.pop()
        except:
            pass
        return aux
