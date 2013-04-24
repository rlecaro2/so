import multiprocessing
import dispatcher as dp
import scheduler as sch
import fileManager as fm
from proceso import Proceso
from realizarLlamada import realizarLlamada 
from recibirLlamada import recibirLlamada 
from enviarMensaje import enviarMensaje
from recibirMensaje import recibirMensaje
from agregarContacto import agregarContacto 
from otro import otro
from enviarPosicion import enviarPosicion
from verPosicion import verPosicion
from juego import juego
from musica import musica

class iOS:  

  def __init__(self, num, instruction, procesoNuevo):  
    self.instruction = instruction
    self.procesoNuevo = procesoNuevo
    self.sharedTimer = num
    self.running = True
    # Cola ready de los procesos
    self.ready=[]
    #self.historial
    self.scheduler= sch.Scheduler()
    self.dispatcher = dp.Dispatcher()
    self.fecha = 0

  def Start(self):
    while (self.running):
      msg = self.instruction.value
      pro = self.procesoNuevo.value
      if len(msg)>0 :
        if(str(msg).startswith('file')):
          self.addFile(msg.split(';')[1])
          self.instruction.value = ""
        elif (str(msg) == "top"):
          self.top()
          self.instruction.value = ""
        elif (str(msg) == "exit"):
          print "Adios!"
          self.running = False  

      if len(self.procesoNuevo.value) > 0:
        self.crearProcesoNuevo()

      self.Run()

  def crearProcesoNuevo(self):
    cmd = str(self.procesoNuevo.value)
    data = cmd.split(';')
    tipo = int(data[2])
    if tipo == 1:
        proc = realizarLlamada(data)
    elif tipo == 2:
        proc = recibirLlamada(data)
    elif tipo == 3:
        proc = enviarMensaje(data)
    elif tipo == 4:
        proc = recibirMensaje(data)
    elif tipo == 5:
        proc = agregarContacto(data)
    elif tipo == 6:
        proc = otro(data)
    elif tipo == 7:
        proc = enviarPosicion(data)
    elif tipo == 8:
        proc = verPosicion(data)
    elif tipo == 9:
        proc = juego(data)
    elif tipo == 10:
        proc = musica(data)

    self.Insertar_en_ColaReady(proc)
    self.procesoNuevo.value = ""

  def addFile(self, filename):     
      # Al hacer esto el scheduler lee el input y agenda los procesos ordenadamente
      self.scheduler.AgendarProcesos(filename)         
  
  def Run(self):
    tempready = self.scheduler.Procesos_a_ejecutar(self.fecha)
          # Insertamos en la cola ready los procesos que ya se gatillaron
    for p in tempready:
        self.Insertar_en_ColaReady(p)
  
    if (len(self.ready)>0):
        # Si no hay nada en running ingresamos un proceso a este
        if(self.dispatcher.estadorunning == False):
            self.dispatcher.Proceso_a_Running(self.ready[0])
        else:
            ## Recordar que cero es la mayor prioridad por lo tanto mayor numero de prioridad indica prioridad mas baja
            if(self.dispatcher.PrioridadProceso()>self.ready[0]):
                tempprocess = self.dispatcher.Interumpir_proceso(self.ready[0])
                self.Insertar_en_ColaReady(tempprocess)

    self.dispatcher.Ejecucion_proceso()                                             
    self.fecha += 1
    self.sharedTimer.value = self.fecha
  
  ## La cola ready esta ordena por prioridad
  ## M?todo que inserta de forma ordena los m?todo en ready, de acuerdo con su prioridad y fecha llegada a la cola
  ## Fecha llegada == Fecha ejecucion 
  def Insertar_en_ColaReady(self, process):
        if(len(self.ready) == 0):
            self.ready.append(process)
        else:
            ## Esto es solo en caso que deba ir al final de la fila, para no tener que recorrerla entera
            if(process.prioridad<self.ready[len(self.ready)-1].prioridad):
                self.ready.insert(len(self.ready)-1,process)
                for i in range (1, len(self.ready)-2):
                    if(process.prioridad()<self.ready[i].prioridad()):
                        self.ready.insert(i,process)

  def top(self):
        p = self.dispatcher.running
        left = p.duracion - p.t_running
        print "process - time left"
        if left > 0:
          print "> " + p.nombre + " - " + str(left) 
        for proc in self.ready:
            left = proc.duracion - proc.t_running
            if left > 0:
              print "> " + proc.nombre + " - " + str(left)
        print "----------------------------" 


