from fileManager import fileManager as fm
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

class Scheduler:
   
    def __init__(self):
       #Cola de procesos del tipo lista
        self.procesos = []

    #Metodo que usar leerInput este le entrega la lista de procesos, lo cuales los en la cola de procesos de acuerdo a la fecha de ejecuci?n 

    def AgendarProcesos(self, filename):        
        tempprocesos = self.leerInput(filename)

        inserted = False       
        for process in tempprocesos:         
            inserted = False
            for p in self.procesos:
                if not inserted and process.fecha < p.fecha:
                    self.procesos.insert(self.procesos.index(p),process)
                    inserted = True
            if not inserted:
                self.procesos.append(process)

    #Revisa la lista de procesos y devuelve aquellos que se deben ejecutar en la fech recibida
    def Procesos_a_ejecutar(self, date):
        listaejecucion = []        
        for p in self.procesos:
            if(p.fecha <= date):
                listaejecucion.append(p)
                self.procesos.remove(p)     
        return listaejecucion
        
    # Metodo que retorna la lista de prorcesos instanciada
    def leerInput(self, filename):
        stack = fm.leerInput(filename)
        listaProcesos = []
        #hacer hashtable si hay tiempo
        for data in stack:    
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

            if proc:
                listaProcesos.append(proc)

        return listaProcesos
