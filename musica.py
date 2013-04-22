from Proceso import Proceso

class musica(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = args[4]

        #variables especificas de musica