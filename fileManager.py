class fileManager:

  @staticmethod
  def _appendToFile(filename, content):
    target = open(filename, "a")
    target.write(content)
    target.close()

  @staticmethod
  def registrarLlamada(content):
    _appendToFile("llamadas.txt", content)

  @staticmethod
  def leerInput(filename): #devuelve stack de procesos
    target = open(filename,"r")
    line = target.readline()
    stack = []
    while (line != ''):
      attr = line.split(',')
      stack.append(attr)

    return stack




      


