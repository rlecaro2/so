

class helpers:

  @staticmethod
  def sortByDate(x, y):
    if(x.fecha == y.fecha):
      return  x.prioridad - y.prioridad
    else:
      return x.fecha - y.fecha

  @staticmethod
  def sortByPriority(x, y):
    return x.prioridad - y.prioridad