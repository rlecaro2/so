import proceso as p
class Dispatcher:
  
     

    #Constructor
    def __init__(self):
        self.estadorunning= False
    
        #Se debe respaldar el proceso en ejecuci?n, se empieza con un proceso en defecto
        self.running=p.Proceso("nn",6,10,0)

   #Pone el proceso en running
    def Proceso_a_Running(self,proceso):
        self.running= proceso
        self.estadorunning=True;        

    #Actualiza los datos del proceso en ejecuci?n
    def Ejecucion_proceso(self):

        if(self.running.get_trunning()!=self.running.get_duracion()):
            self.running.add1_to_trunning()
        else:
            self.Terminar_proceso()

    #Entrega los datos del proceso que estan en running
    def PrioridadProceso(self):
        return self.running.get_prioridad()

    #Cuando llega un proceso de menor prioridad quita el proceso en ejecuci?n, para ello respalda de la informo de este proceso para cuando 
    #tenga q volver a ser ejecutado y lo retorno para que entre en la cola ready
    def Interumpir_proceso(self, proceso):
        self.temporal=self.running
        self.running=proceso
        return self.temporal

    #cuando termina de ejecutarse un proceso este metodo vacia el running
    def Terminar_proceso(self): 
        self.estadorunning=False
        
