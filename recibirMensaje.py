from proceso import Proceso
from fileManager import fileManager
from time import localtime, strftime
import math

class recibirMensaje(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)

        self.numero = args[4]
        self.mensaje = args[5]
        self.duracion = math.ceil(len(self.mensaje)*0.02)
        #variables especificas de mensaje
     
    def imprimir(self):
        return strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - Mensaje recibido de: " + self.numero +  ", mensaje: \"" + self.mensaje + "\"\n"     

    #Metodo que guarda el mensaje en la memoria del celular (archivo de texto)
    
    def guardar_en_memoria(self):
        fileManager.appendToFile("Historial_Mensajes.txt", self.imprimir())

    def finish(self):
        fileManager.appendToFile("Log.txt", self.imprimir())
        self.guardar_en_memoria()