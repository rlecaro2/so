from proceso import Proceso

class realizarLlamada(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)

        self.numero = args[4]
        self.duracion = int(args[5])

        #variables especificas de llamadas
    def imprimir(self):
            return self.fecha + " - Llamada realizada al numero: " + self.numero + ". Duracion: " + str(self.duracion) + " segundos."