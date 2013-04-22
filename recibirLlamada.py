from Proceso import Proceso

class recibirLlamada(Proceso):
    def __init__(self, args):        
        super(recibirLlamada, self).__init__(args)

        self.numero = args[4].split(';')[0]
        self.duracion = args[4].split(';')[1]

        #variables especificas de llamadas