from Proceso import Proceso

class verPosicion(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = args[4]
