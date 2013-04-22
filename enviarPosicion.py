from Proceso import Proceso

class enviarPosicion(Proceso):
    def __init__(self, args):        
        super(enviarPosicion, self).__init__(args)
        self.duracion = 2
