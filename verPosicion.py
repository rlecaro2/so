from proceso import Proceso

class verPosicion(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = int(args[4])

    def imprimir(self):
            return self.fecha + " - Posicion revisada durante " + str(self.duracion) + " segundos."