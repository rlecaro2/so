from proceso import Proceso

class otro(Proceso):
    def __init__(self,args):
        Proceso.__init__(self,args)
        self.duracion = int(args[4])
    
    def imprimir(self):
        return self.fecha + " - Cualquier proceso durante " + str(self.duracion) + " segundos."