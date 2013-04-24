from proceso import Proceso
from fileManager import fileManager

class juego(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = int(args[4])
        #variables especificas de juego    
    def imprimir(self):
            return strftime("%Y-%m-%d %H:%M:%S", localtime()) + " - Juego durante " + str(self.duracion) + " segundos."

