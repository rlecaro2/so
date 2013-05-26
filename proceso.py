from fileManager import fileManager
from time import localtime, strftime
import time
import threading

class Proceso:
  
    ## la secuencia de los argumentos variables debe ser duracion,numero de contacto al que se manda o del q se recibe, mensaje
    ## Ojo que estos argumentos pueden ponerso o no

  def __init__(self, args):
    self.nombre = args[0]
    self.fecha = int(args[1])
    self.tipo = int(args[2])
    self.recursos = {}
    self.setRecursos()
    self.prioridad = int(args[3])
    self.run = threading.Event() #evento que gatillare para avisarle al proceso que corra
    self.finished = False
    self.thread = threading.Thread(name = self.nombre, target = self.runProcess)
    
    if(self.nombre != "nn"):
      self.thread.start()
    #variables comunes a todo proceso
    self.duracion = 0
    
    self.t_inicio = 0
    self.t_fin = 0
    #Este variable nos dice cuanto tiempo ha estado en running (Sirve para cuando hay expropiacion)
    
    self.t_running = 0
    
    #Si el proceso no esta en ejecucion su running es False
    self.running = False

  def add1_to_trunning(self):
    self.t_running += 1
    time.sleep(1)


  def runProcess(self):
    while not self.finished:
      self.run.wait() #espero permiso para correr
      if(self.t_running != self.duracion):
          self.add1_to_trunning()
      else:
          self.finish()
          self.finished = True

  def finish(self):
    pass

  def setRecursos(self):    
    if (self.tipo == 1 or self.tipo == 2):
      self.recursos = { "pantalla" : "U", "audifono" : "B", "microfono" : "B", "enviar info" : "U", "recibir info" : "U" }
    elif self.tipo == 3 or self.tipo == 4:
      self.recursos = { "audifono" : "U", "enviar info" : "U", "recibir info" : "U" }
    elif self.tipo == 5:
      self.recursos = { "pantalla" : "U" }
    elif self.tipo == 6:
      self.recursos = { "pantalla" : "N", "audifono" : "U", "microfono" : "U", "GPS" : "U", "enviar info" : "U", "recibir info" : "U" }  
    elif self.tipo == 7:
      self.recursos = { "GPS" : "U", "enviar info" : "U" }
    elif self.tipo == 8:
      self.recursos = { "pantalla" : "U", "GPS" : "U" }
    elif self.tipo == 9:
      self.recursos = { "pantalla" : "N", "audifono" : "U", "GPS" : "U", "enviar info" : "U", "recibir info" : "U" }
    elif self.tipo == 10:
      self.recursos = { "pantalla" : "U", "audifono" : "U", }
    else:
      self.recursos = {"pantalla": "U"}

        
     
    

