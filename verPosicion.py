from Proceso import Proceso

class verPosicion(Proceso):
    def __init__(self, args):        
        super(verPosicion, self).__init__(args)
        self.duracion = args[4]
