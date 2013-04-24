from proceso import Proceso
from fileManager import fileManager
from time import localtime, strftime

class verPosicion(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = int(args[4])

    def imprimir(self):
            return strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - Posicion revisada durante " + str(self.duracion) + " segundos."

    def finish(self):
        fileManager.appendToFile("Log.txt", self.imprimir())