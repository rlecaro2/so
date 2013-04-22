import Proceso

class consola(Proceso):
    def __init__(self):
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