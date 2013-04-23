from proceso import Proceso
import fileManager

class recibirLlamada(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)

        self.numero = args[4]
        self.duracion = int(args[5])

        #variables especificas de llamadas
    def imprimir(self):
        return self.fecha + " - Llamada recibida de: " + self.numero + ". Duracion: " + str(self.duracion) + " segundos."
    
    def guardar_en_memoria(self):
        fileManager.appendToFile("Historial_Llamadas.txt", imprimir())
        
    def finish(self):
        guardar_en_memoria()