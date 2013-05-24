from fileManager import fileManager
from time import localtime, strftime
import time

class Proceso:
  
    ## la secuencia de los argumentos variables debe ser duracion,numero de contacto al que se manda o del q se recibe, mensaje
    ## Ojo que estos argumentos pueden ponerso o no

  def __init__(self, args):
    self.nombre = args[0]
    self.fecha = int(args[1])
    self.tipo = args[2]
    self.recursos = self.setRecursos()
    self.prioridad = int(args[3])
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

  def finish(self):
    pass

  def setRecursos(self):
    if self.tipo == 1 or self.tipo == 2:
      return     
      {
        "pantalla" : "U",
        "audifono" : "B",
        "microfono" : "B",        
        "enviar info" : "U",
        "recibir info" : "U"
      }
    elif self.tipo == 3 or self.tipo == 4:
      return
      {
        "audifono" : "U",
        "enviar info" : "U",
        "recibir info" : "U"
      }
    elif self.tipo == 5:
      return { "pantalla" : "U" }
    elif self.tipo == 6:
      return     
      {
        "pantalla" : "N",
        "audifono" : "U",
        "microfono" : "U", 
        "GPS" : "U",
        "enviar info" : "U",
        "recibir info" : "U"
      }  
    elif self.tipo == 7:
      return     
      {
        "GPS" : "U",
        "enviar info" : "U"
      }
    elif self.tipo == 8:
      return     
      {
        "pantalla" : "U",
        "GPS" : "U"
      }
    elif self.tipo == 9:
      return    
      {
        "pantalla" : "N",
        "audifono" : "U",
        "GPS" : "U",
        "enviar info" : "U",
        "recibir info" : "U"
      }
    elif self.tipo == 10:
      return     
      {
        "pantalla" : "U",
        "audifono" : "U",
      }
        
     
    

