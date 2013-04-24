from proceso import Proceso
from fileManager import fileManager
from time import localtime, strftime

class realizarLlamada(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)

        self.numero = args[4]
        self.duracion = int(args[5])

        #variables especificas de llamadas
    def imprimir(self):
        return strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - Llamada realizada a: " + self.numero + ". Duracion: " + str(self.duracion) + " segundos. \n"
    
    def guardar_en_memoria(self):
        fileManager.appendToFile("Historial_Llamadas.txt", self.imprimir())
        
    def finish(self):
        self.guardar_en_memoria()