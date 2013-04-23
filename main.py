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
    
     
    
