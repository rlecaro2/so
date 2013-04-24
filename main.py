from iOS import iOS 
from consola import consola
from multiprocessing import Manager, Process, Value
from fileManager import fileManager as fm

if __name__ == "__main__":
    fm.clearTxt()
  with Manager() as Manager:
    num = Manager.Value('i', 0)
    procesoNuevo = Manager.Value(unicode, '')
    instruction = Manager.Value(unicode, '')
    console = consola(num, instruction, procesoNuevo)
    os = iOS(num, instruction, procesoNuevo)
    process1 = Process(target = os.Start)
    process1.start()
    console.Run()
    process1.join()    
     
    
