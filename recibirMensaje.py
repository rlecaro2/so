from Proceso import Proceso

class recibirMensaje(Proceso):
    def __init__(self, args):        
        super(recibirMensaje, self).__init__(args)

        self.numero = args[4].split(';')[0]
        self.mensaje = args[4].split(';')[1]
        self.duracion = len(self.mensaje)*20
        #variables especificas de mensaje
        
    #Metodo que guarda el mensaje en la memoria del celular (archivo de texto)
    def guardar_en_memoria():
        pass