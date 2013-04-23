from proceso import Proceso

class juego(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = int(args[4])
        #variables especificas de juego    
    def imprimir(self):
            return self.fecha + " - Juego durante " + str(self.duracion) + " segundos."