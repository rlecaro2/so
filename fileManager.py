class fileManager:

  @staticmethod
  def _appendToFile(filename, content):
    target = open(filename, "a")
    target.write(content)
    target.close()

  @staticmethod
  def registerCall(number, timestamp, incoming):
    pass
