from Proceso import Proceso

class agregarContacto(Proceso):
    def __init__(self, args):        
        super(agregarContacto, self).__init__(args)

        self.nombreContacto = args[4].split(';')[0]
        self.numeroContacto = args[4].split(';')[1]

        #variables especificas de llamadas