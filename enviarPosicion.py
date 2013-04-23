from proceso import Proceso

class enviarPosicion(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = 2

    def imprimir(self):
        return self.fecha + " - Posicion enviada."