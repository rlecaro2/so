from socket import socket, AF_INET, SOCK_STREAM 
import  sys , threading

class Servidor:
           
    def  __init__(self, port, ip, Num_connec):
        threading.Thread.__init__(self)
        self.puerto= port
        self.IP= ip
        self.servidor = socket(AF_INET,SOCK_STREAM)
        self.ProcesosRecibidos = []
              
        try: 
            self.servidor.bind((self.IP, self.puerto))
            self.servidor.listen(Num_connec)

        except socket.error:
            print('Bind failed %s' % (socket.error))
            sys.exit()


    def escuchar_cliente(self):
           
            while True:
                data = client.recv(1024)
                print("Instruccion recibida: "+ data)                     
            client.close() 

    def enviar_mensajes(self, msj):
        
        mensaje= msj
        self.socket.send(mensaje)

    def llamar(self):
        pass

    def terminarllamada(self):
        pass


    def finalizarconexion():
        self.servidor.close()
        threading.Thread._Thread__stop()
        
   
    def run(self):

        threading.Thread(target= self.escuchar_cliente).start()
    
    def GetIntruccionesRecibidas(self):
        aux = ProcesosRecibidos.pop()
        return aux


    

