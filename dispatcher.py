import proceso as p

class Dispatcher:     

    #Constructor
    def __init__(self):
        self.estadorunning = False
        self.paloBlanco = p.Proceso(["nn",6,10,0])
        #Se debe respaldar el proceso en ejecuci?n, se empieza con un proceso en defecto
        self.running = p.Proceso(["nn",6,10,0])
        self.estados_IO = {
          "pantalla" : "D",
          "audifono" : "D",
          "microfono" : "D", 
          "GPS" : "D",
          "enviar info" : "D",
          "recibir info" : "D"
          }


   #Pone el proceso en running ordenado por prioridad, el primero sera el de mayor y el ultimo el de menor
    def Proceso_a_Running(self,proceso):
        self.running = proceso
        self.estadorunning = True;        

    #Actualiza los datos del proceso en ejecuci?n
    ## si correponde que el proceso debe terminar, lo termina 
    def Ejecucion_proceso(self):
        if(self.running.t_running != self.running.duracion):
            self.running.add1_to_trunning()
        else:
            self.Terminar_proceso()

    #Entrega los datos del proceso que estan en running
    def PrioridadProceso(self):
        return self.running.prioridad

    #Cuando llega un proceso de menor prioridad quita el proceso en ejecuci?n, para ello respalda de la informo de este proceso para cuando 
    #tenga q volver a ser ejecutado y lo retorno para que entre en la cola ready
    def Interumpir_proceso(self, proceso):
        self.temporal = self.running
        self.running = proceso
        return self.temporal

    #cuando termina de ejecutarse un proceso este metodo vacia el running
    def Terminar_proceso(self): 
        self.estadorunning = False
        self.running.finish()
        self.running = self.paloBlanco
    
 
    ##Si un proceso puede ingresar este metodo lo mete en running y saca aquellos que no puedan estar cn el, en caso 
    ## de que no debe salir ninguno, retorna una lista vacia
    def IngresarYsacarProcesos(self, proceso):
        
        procesos_fuera=[]
        for i in range(0, len(self.running)):
            if(self.PuedenFuncionarJuntos(proceso, self.running[i]) == False):
                if(self.running[i].prioridad<proceso.prioridad):
                    procesos_fuera.append(self.running[i])
                    running.pop(i)

        ##Hay que modificar este metodo para que ingrese los procesos en la lista ordenados por prioridad, recordar que el actual
        ##Solo aguanta un proceso
        self.Proceso_a_Running(proceso)
        return procesos_fuera 
    ##assDetermina si es facible ingresar un proceso a running
    def PuedeEntrarEnRunning(self, proceso):
        
        ##vemos si el proceso actual puede funcionar con todos los procesos que estan dentro              
        for p in self.running:
            ##guardamos para cada proceso en running si puede funcionar con el
            respuesta.append ( self.PuedenFuncionarJuntos(proceso,p))
        for i in range(0,len(respuesta)):
            if(respuesta[i] == False):
                if(self.running[i].prioridad>proceso.prioridad):
                   return False
            else:
                   return True
                   


    def PuedenFuncionarJuntos(self,P1,P2):

      temp_recursos1 = P1.setRecursos()
      temp_recursos2 = P2.setRecursos()
      recursos = P1.keys();
      
      for key in recursos:
          
          if(temp_recursos2.has_key(key)):
              ##Evaluar de acuerdo a la tabla si pueden estar juntos operando
              if(temp_recursos1.get(key)=="B" | temp_recusos2.get(key)=="B"): 
                  return False;
              elif(temp_recursos1.get(key)=="N" & temp_recusos2.get(key)=="N"):
                  return False  
              else:
                  return True
 
  