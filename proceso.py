
class Proceso:
  
    ## la secuencia de los argumentos variables debe ser duracion,numero de contacto al que se manda o del q se recibe, mensaje
    ## Ojo que estos argumentos pueden ponerso o no

  def __init__(self, args):
    self.nombre = args[0]
    self.fecha = args[1]
    self.tipo = args[2]
    self.prioridad = args[3]
    #variables comunes a todo proceso

    self.t_inicio = 0
    self.t_fin = 0
    #Este variable nos dice cuanto tiempo ha estado en running (Sirve para cuando hay expropiacion)
    
    self.t_running = 0
    
    #Si el proceso no esta en ejecucion su running es False
    self.running = False

  def add1_to_trunning(self):

       self.t_running=t_running+1


        
     
    

