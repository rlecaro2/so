
class Proceso:
  
    ## la secuencia de los argumentos variables debe ser duracion,numero de contacto al que se manda o del q se recibe, mensaje
    ## Ojo que estos argumentos pueden ponerso o no

  def __init__(self, nombre, tipo, prioridad, fechaejecucion, *args):
    self.nombre = nombre
    self.tipo = tipo
    self.prioridad = prioridad
    self.fecha=fechaejecucion
     
    #Variables comunes para todo proceso
    # *arguments -> esto es para numero de argumentos variables   
    self.duracion=args[1]
    self.numero=args[2]
    self.msj=args[3]
    self.t_inicio=0
    self.t_fin=0
    #Este variable no dice cuanto tiempo ha estado en running (Sirve para cuando hay expropiasi?n)
    self.t_running=0
    #Si el proceso no esta en ejecuci?n su estado es False
    self.estado=False

  def get_trunning(self):
        return self.t_running

  def add1_to_trunning(self):
        self.running+=1

  def get_duracion(self):
      return self.duracion
  def get_prioridad(self):
      return self.prioridad
        
     
    

