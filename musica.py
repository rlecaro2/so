from proceso import Proceso

class musica(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        self.duracion = int(args[4])
        #variables especificas de musica
    def imprimir(self):
            return self.fecha + " - Musica durante " + str(self.duracion) + " segundos."