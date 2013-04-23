from proceso import Proceso
import fileManager

class realizarLlamada(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)

        self.numero = args[4]
        self.duracion = int(args[5])

        #variables especificas de llamadas
    def imprimir(self):
            return self.t_inicio + " - Llamada realizada a: " + self.numero + ". Duracion: " + str(self.duracion) + " segundos."
    def guardar_en_memoria(self):
        fileManager.appendToFile("Historial_Llamadas.txt", imprimir()):