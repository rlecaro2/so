from proceso import Proceso
from fileManager import fileManager
from time import localtime, strftime

class enviarPosicion(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = 2

    def imprimir(self):
        return strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - Posicion enviada."