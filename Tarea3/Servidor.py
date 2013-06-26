from socket import socket, AF_INET, SOCK_STREAM 
import  sys , threading

class Servidor(threading.Thread):
           
    def  __init__(self, port, ip, Num_connec):
        self.puerto= port
        self.IP= ip
        self.servidor = socket(AF_INET,SOCK_STREAM)
        self.ProcesosRecibidos = []
              
        try: 
            self.servidor.bind((self.IP, self.puerto))
            self.servidor.listen(Num_connec)
            print("Esperando Conexiones ...\n")


        except:
            print('Bind failed')
            sys.exit()


    def escuchar_cliente(self):           
            while True:
                data = self.client.recv(1024)                    
            client.close() 

    def enviar_mensaje(self, msj):        
        mensaje= msj
        self.client.send(mensaje)


    def finalizarconexion():
        self.servidor.close()
        threading.Thread._Thread__stop()
        
    def run(self):
        self.client, addr = self.servidor.accept()
        threading.Thread(target= self.escuchar_cliente).start()
  
    
    def GetIntruccionesRecibidas(self):
        aux = ""
        try:
            aux = self.ProcesosRecibidos.pop()
        except:
            pass
        return aux


    

