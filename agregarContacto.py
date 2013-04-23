from proceso import Proceso
import fileManager

class agregarContacto(Proceso):
    def __init__(self, args):        
        Proceso.__init__(self,args)
        
        self.nombreContacto = args[4]
        self.numeroContacto = args[5]

        #variables especificas de llamadas

    def imprimir(self):
        return " Contacto agregado. Nombre: " + self.nombreContacto + ", numero: " + self.numeroContacto +"."

    def content(self):
    	return self.nombreContacto + ";" + self.numeroContacto

    def guardar_en_memoria():
        fileManager.appendToFile("Agenda_Telefonica", content()):