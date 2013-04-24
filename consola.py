
from fileManager import fileManager as fm
from proceso import Proceso
from realizarLlamada import realizarLlamada 
from recibirLlamada import recibirLlamada 
from enviarMensaje import enviarMensaje
from recibirMensaje import recibirMensaje
from agregarContacto import agregarContacto 
from otro import otro
from enviarPosicion import enviarPosicion
from verPosicion import verPosicion
from juego import juego
from musica import musica

class consola():
    def __init__(self, num, instruction, procesoNuevo):
        self.instruction = instruction
        self.procesoNuevo = procesoNuevo
        self.sharedTimer = num
        self.running = True

    def Run(self):        
        while(self.running):
            command = raw_input("> ")
            if(command.startswith("llamar")):
                try:
                    numero = command.split(" ")[1]
                    duracion = command.split(" ")[2]
                    self.crearLlamada(numero,duracion)                
                except:
                    print "Uso: \"> llamar numero duracion(en segundos)\""
            elif(command.startswith("mensaje")):
                try:
                    numero = numero = command.split(" ")[1]
                    mensaje = command.split(" ")[2]
                    self.crearMensaje(numero,mensaje)
                except:
                    print "Uso: \"> mensaje numero mensaje_a_enviar\"" 
            elif(command == "exit"):
                self.instruction.value = "exit"
                self.running = False
            elif(command.startswith("archivo")):
                try:
                    filename = command.split(" ")[1]
                    self.cargarArchivo(filename)
                except:
                    print "Uso: \"> archivo nombreArchivo\""
            elif(command == "top"):
                self.instruction.value = "top"




    def crearLlamada(self,numero,duracion):
        llamada = "llamada"+";"+str(self.sharedTimer.value)+";"+str(1)+";"+str(0)+";"+str(numero)+";"+str(duracion)
        self.procesoNuevo.value = llamada
    def crearMensaje(self,numero,mensaje):
        mensaje = "mensaje" + ";" + str(self.sharedTimer.value)+";"+str(3)+";"+str(2)+";"+str(numero)+";"+str(mensaje)
        self.procesoNuevo.value = mensaje
    def cargarArchivo(self,filename):
        self.instruction.value = "file;" + filename