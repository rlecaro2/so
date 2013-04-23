from iOS import iOS 
from consola import consola
import thread 

def ProcesoConsola():
     command = raw_input("> ")

     while(command != "exit"):
         if(command.startswith("llamar")):
             try:
                 numero = command.split(" ")[1]
                 duracion = command.split(" ")[2]
           
                 #crear proceso y llamar
             except:
                 print "Uso: \"> llamar numero duracion(en segundos)\""

         elif(command.startswith("mensaje")):
              try:
                   numero = numero = command.split(" ")[1]
                   msj = command.split(" ")[2]
                   #crear proceso y dejar mandando el msj
              except:
                  print "Uso: \"> mensaje numero mensaje_a_enviar\""

     command = raw_input("> ")
     
        


if __name__ == "__main__":
    
    console= consola()
    # Esto es para q el proceso de consola corra en paralelo
    archivo= input("Ingrese nombre de archivo: ")
    thread.start_new_thread(console.Start(),())
    SO= iOS()
    SO.startProcess(archivo)
        
        # FALTA
        #4.	Procesos ingresados por consola se le entregan al scheduler con fecha de ejecuci?n igual a la actual 
