from Proceso import Proceso

class recibirLlamada(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)

        self.numero = args[4]
        self.duracion = args[5]

        #variables especificas de llamadas