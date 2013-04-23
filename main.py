from iOS import iOS 
from consola import consola
from multiprocessing import Process, Queue, Value 

if __name__ == "__main__":
    queue = Queue() 
    num = Value('i', 0)
    console = consola(queue, num)
    os = iOS(queue, num)
    process1 = Process(target = os.Start)
    process1.start()
    console.Run()
    process1.join()
    
     
    
<<<<<<< HEAD
=======
    console= consola()
    # Esto es para q el proceso de consola corra en paralelo
    archivo= raw_input("Ingrese nombre de archivo: ")
    thread.start_new_thread(console.Start(),())
    SO= iOS()
    SO.startProcess(archivo)

>>>>>>> d5f75ec73405acd2817ad4835dd10ef02b820cd5
