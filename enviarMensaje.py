from proceso import Proceso

class enviarMensaje(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)

        self.numero = args[4]
        self.mensaje = args[5]
        self.duracion = len(self.mensaje)*20
        #variables especificas de mensaje
    
    def imprimir(self):
            return self.fecha + " - Mensaje enviado al numero: " + self.numero + ". Contenido: \"" + self.mensaje + "\"."  
    #Metodo que guarda el mensaje en la memoria del celular (archivo de texto)
    def guardar_en_memoria():
        pass