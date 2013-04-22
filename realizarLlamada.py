from Proceso import Proceso

class realizarLlamada(Proceso):
    def __init__(self, args):        
        super(realizarLlamada, self).__init__(args)

        self.numero = args[4].split(';')[0]
        self.duracion = args[4].split(';')[1]

        #variables especificas de llamadas