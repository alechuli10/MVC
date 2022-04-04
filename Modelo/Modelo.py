class Modelo:
  def __init__ (self):
    self.__listaMensajes= []

  def agregarMensaje (self,mensaje):
    self.__listaMensajes.append(mensaje.upper())

  def getListaMensajes (self):
    return self.__listaMensajes
    