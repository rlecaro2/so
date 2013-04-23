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

    self.dispatcher = dp.Dispatcher()
    #self.schedululer = sch.Scheduler

  def startProcess(info):
    pass

      ## Esta secuencia de bloque corresponde a cuando se hace una interrupc?on de proceso
      ## Esta secuencia de bloque corresponde a cuando se hace una interrupcion de proceso

      

    
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


  ## M?todo que inserta de forma ordena los m?todo en ready, de acuerdo con su prioridad y fecha llegada a la cola
  ## Fecha llegada == Fecha ejecucion 
  def Insertar_en_ColaReady(self, process):

      if(len(ready) == 0):
          ready.append(process)
      
      else:
      ## Esto es solo en caso que deba ir al final de la fila, para no tener que recorrerla entera
          if(process.get_prioridad()<ready[len(self.ready)-1].get_prioridad()):
             ready.insert(len(self.ready)-1,process)
          
          for i in range (1, len(self.ready)-2):
          
             if(process.get_prioridad()<ready[i].get_prioridad()):

                 ready.insert(i,process)
                           
           

      
      

     
