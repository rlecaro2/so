from socket import socket, AF_INET, SOCK_STREAM 
import  sys , threading

class Servidor(threading.Thread):


   
    def  __init__(self, port, ip, Num_connec):
        threading.Thread.__init__(self)
        self.puerto= port
        self.IP= ip
        self.servidor = socket(AF_INET,SOCK_STREAM)
        self.clientes = [] # current connections
        self.n_clientes=0
        
        try: 
            self.servidor.bind((self.IP, self.puerto))
            self.servidor.listen(Num_connec)

        except socket.error:
            print('Bind failed %s' % (socket.error))
            sys.exit()
 



    def escuchar_cliente(self, client, addr):
           
            while True:
                data = client.recv(1024)
                print("Cliente "+ data)
                #conn.sendall(reply)
                for c in self.clientes:
                    if c != client :
                        c.sendall(data)             
            client.close() 

    def run(self):
      
       
        while True:
            client, addr = self.servidor.accept()
            threading.Thread(target=self.escuchar_cliente, args=(client, addr)).start()
            # agregamos una lista con las conexiones
            
            self.clientes.append(client)

    def finalizarconexion():
        self.servidor.close()




