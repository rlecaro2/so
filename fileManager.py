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
  def registrarLlamada(llamada):
    content = str(llamada.fecha) + " " + str(llamada.t_inicio) + str() 
    _appendToFile("llamadas.txt", content)

  @staticmethod
  def almacenarContacto(nombre,numero):
    content = nombre + ";" + numero + "\n"
    _appendToFile("contactos.txt",content)





      

