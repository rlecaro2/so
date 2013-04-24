from proceso import Proceso
from fileManager import fileManager
from time import localtime, strftime

class musica(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = int(args[4])
        #variables especificas de musica
    def imprimir(self):
            return strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - Musica durante " + str(self.duracion) + " segundos."
    
    def finish(self):
        fileManager.appendToFile("Log.txt", self.imprimir())