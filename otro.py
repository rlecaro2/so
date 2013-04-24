from proceso import Proceso
from fileManager import fileManager

class otro(Proceso):
    def __init__(self,args):
        Proceso.__init__(self,args)
        self.duracion = int(args[4])
    
    def imprimir(self):
        return strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - Cualquier proceso durante " + str(self.duracion) + " segundos."