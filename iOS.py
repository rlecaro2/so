import os, time
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
import threading
from helpers import helpers

class iOS:  

  def __init__(self, num, instruction, procesoNuevo):  
    self.instruction = instruction
    self.procesoNuevo = procesoNuevo
    self.sharedTimer = num
    self.running = True
  
    # Cola ready de los procesos
    self.ready = []
    #Cola waiting
    self.waiting = [] 
    #self.historial
    self.scheduler = sch.Scheduler()
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

    self.waiting.append(proc)
    self.procesoNuevo.value = ""

  def addFile(self, filename):     
      # Al hacer esto el scheduler lee el input y agenda los procesos ordenadamente
      self.scheduler.AgendarProcesos(filename)       
  
  def Run(self):
    self.limpiarRunning()
    self.ready += (self.scheduler.Procesos_a_ejecutar(self.fecha)) #Entran a esperar los procesos que corresponda

    #self.waiting = sorted(self.waiting, cmp = helpers.sortByPriority)

    #la cola waiting se reordena segun el criterio que se ocupe en cmp
    for w in self.waiting: #si hay algun proceso en waiting
        if(self.dispatcher.PuedeEntrarEnRunning(w)):#si puede entrar a correr
            self.waiting += (self.dispatcher.IngresarYsacarProcesos(w)) #entra y los que salen se ponen en waiting (despues los ordenamos)
            self.waiting.pop(self.waiting.index(w)) #se saca de waiting el proceso que acaba de entrar

    for r in self.ready:
      if(self.dispatcher.PuedeEntrarEnRunning(r)):#si puede entrar a correr
            self.waiting += (self.dispatcher.IngresarYsacarProcesos(r)) #entra y los que salen se ponen en waiting (despues los ordenamos)
            self.ready.pop(self.ready.index(r)) #se saca de waiting el proceso que acaba de entrar

    self.fecha += 1
    self.sharedTimer.value = self.fecha
  
  ## La cola ready esta ordena por prioridad
  ## M?todo que inserta de forma ordena los m?todo en ready, de acuerdo con su prioridad y fecha llegada a la cola
  ## Fecha llegada == Fecha ejecucion 
  def Insertar_en_ColaReady(self, process):
        inserted = False
        for p in self.ready:
          if not inserted and process.prioridad < p.prioridad:
            self.ready.insert(self.ready.index(p),process)
            inserted = True
        if not inserted:
          self.ready.append(process)

  def limpiarRunning(self):
    for p in self.dispatcher.running:
      if p.finished:
        self.dispatcher.running.remove(p)


  def top(self):

    os.system('cls' if os.name=='nt' else 'clear')
    content = "Running \n"
    content += "process - time left\n"
    content += "----------------------------\n"
    for p in self.dispatcher.running:
        left = p.duracion - p.t_running
        if left > 0:
          content += "> " + p.nombre + " - " + str(int(left)) +"\n"
    content += "---------------------------- \n"     

    content += "Waiting \n"
    content += "process - time left\n"
    content += "----------------------------\n"
    for p in self.waiting:
        left = p.duracion - p.t_running
        if left > 0:
          content += "> " + p.nombre + " - " + str(int(left)) +"\n"
    content += "---------------------------- \n" 

    content += "Ready \n"
    content += "process - time left\n"
    content += "----------------------------\n"
    for p in self.ready:
        left = p.duracion - p.t_running
        if left > 0:
          content += "> " + p.nombre + " - " + str(int(left)) +"\n"
    content += "---------------------------- \n" 
    print content



  
        

       