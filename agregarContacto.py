from proceso import Proceso
from fileManager import fileManager
from time import localtime, strftime

class agregarContacto(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        
        self.nombreContacto = args[4]
        self.numeroContacto = args[5]

        #variables especificas de llamadas

    def imprimir(self):
        return strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - Contacto agregado. Nombre: " + self.nombreContacto + ", numero: " + self.numeroContacto +"."

    def content(self):
    	return self.nombreContacto + ";" + self.numeroContacto

    def guardar_en_memoria(self):
        fileManager.almacenarContacto(self.nombreContacto, self.numeroContacto)

    def finish(self):
        fileManager.appendToFile("Log.txt", self.imprimir())
        self.guardar_en_memoria()