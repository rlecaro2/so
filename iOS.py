import multiprocessing
import dispatcher as dp
import scheduler as sch
import fileManager as fm
from proceso import Proceso

class iOS:
  

  def __init__(self):  
    ## Cola ready de los procesos
    self.ready=[]
    self.historial
    self.scheduler= sch.Scheduler()
    self.dispatcher = dp.Dispatcher()
    #self.schedululer = sch.Scheduler

  def startProcess(self, filename):
     
      ## Al hacer esto el scheduler lee el input y agenda los procesos ordenadamente
      self.scheduler.AgendarProcesos(filename)
      fecha=0 
      while (True):
         
          tempready = self.scheduler.Procesos_a_ejecutar(fecha)
          ## Insertamos en la cola ready los procesos que ya se gatillaron
          for p in tempready:
              self.Insertar_en_ColaReady(p)
        
          if (len(self.ready)>0):

              ## Si no hay nada en runnin ingresamos un proceso a este
              if(self.dispatcher.estadorunning == False):
                  self.dispatcher.Proceso_a_Running(self.ready[0])
              else:
                  ## Recordar que cero es la mayor prioridad por lo tanto mayor número de prioridad indica prioridad mas baja
                  if(self.dispatcher.PrioridadProceso()>self.ready[0]()):
                      tempprocess = self.dispatcher.Interumpir_proceso(self.ready[0])
                      self.Insertar_en_ColaReady(tempprocess)

          self.dispatcher.Ejecucion_proceso()                                             
          fecha=fecha +1
                  
   

  
  ## La cola ready esta ordena por prioridad
  ## M?todo que inserta de forma ordena los m?todo en ready, de acuerdo con su prioridad y fecha llegada a la cola
  ## Fecha llegada == Fecha ejecucion 
  def Insertar_en_ColaReady(self, process):

        if(len(ready) == 0):
            ready.append(process)

        else:
            ## Esto es solo en caso que deba ir al final de la fila, para no tener que recorrerla entera
            if(process.prioridad()<ready[len(self.ready)-1].prioridad()):
                ready.insert(len(self.ready)-1,process)

                for i in range (1, len(self.ready)-2):
                    if(process.prioridad()<ready[i].prioridad()):
                        ready.insert(i,process)


  def top(self):
        p = self.dispatcher.running
        left = p.duracion - p.t_running
        print "process - time left \n"
        print p.nombre + " - " + str(left) + "\n"

        for proc in ready:
            left = proc.duracion - proc.t_running
            print proc.nombre + " - " + str(left) + "\n"


    
  def leerInput(self, filename):
        stack = fm.leerInput(filename)
     self.scheduler = sch.Scheduler(stack)

  def hacerLlamada():
      pass
  def enviarMensaje():
         pass
  def verContactos():
          pass
  def verHistorial():
        pass
  def correr_juego():
      pass

      
      

     
