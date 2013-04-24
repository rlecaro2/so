
class fileManager:

  @staticmethod
  def appendToFile(filename, content):
    target = open(filename, "a")
    target.write(content)
    target.close()

  @staticmethod
  def leerInput(filename): #devuelve stack de procesos
    target = open(filename,"r")
    line = target.readline()
    stack = []
    while len(line.strip()) > 0:
      line = line.strip("\n")
      attr = line.split(';')
      stack.append(attr)
      line = target.readline()
      
    return stack

  @staticmethod
  def almacenarContacto(nombre,numero):
    content = nombre + ";" + numero + "\n"
    target = open("Contactos.txt", "a")
    target.write(content)
    target.close()

  @staticmethod
  def showCalls():
    target = open("Historial_Llamadas.txt",'r')
    line = target.readline()
    while len(line.strip()) > 0:
      print line
      line = target.readline()
    target.close()

  @staticmethod
  def showMessages():
    target = open("Historial_Mensajes.txt",'r')
    line = target.readline()
    while len(line.strip()) > 0:
      print line
      line = target.readline()
    target.close()
      
  @staticmethod
  def showContacts():
    target = open("Contactos.txt",'r')
    stack = []
    line = target.readline()
    i=0
    while len(line.strip()) > 0:
      print "["+i+"] " + line
      stack.append(line)
      line = target.readline()
      i+=1
    target.close()
    return stack




      

