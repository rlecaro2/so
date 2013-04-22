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

  ## Metodo que ordena los metodo en ready, de acuerdo con su prioridad y fecha llegada a la cola
  ## Fecha llegada == Fecha ejecucion 
  
  def OrdenarColaReady(self):
      pass

     
