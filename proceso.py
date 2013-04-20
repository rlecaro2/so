
class Proceso:
  

  def __init__(self, nombre, tipo, prioridad, fechaejecucion):
    self.nombre = nombre
    self.tipo = tipo
    self.prioridad = prioridad
    self.fecha=fechaejecucion
      #Variables comunes para todo proceso

    self.duracion=0
    self.t_inicio=0
    self.t_fin=0
    #Este variable no dice cuanto tiempo ha estado en running (Sirve para cuando hay expropiasión)
    self.t_running=0
    #Si el proceso no esta en ejecución su estado es False
    self.estado=False
     
    

