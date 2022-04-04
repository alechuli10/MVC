class VistaFichero:
  def __init__ (self,nombreFichero):
    self.__nombreFichero= nombreFichero
  
  def abrir (self):
    self.__fichero= open(self.__nombreFichero,"w")

  def cerrar (self):
    self.__fichero.close()

  def escribirLineas (self,lineas):
    for linea in lineas:   
      self.__fichero.write(linea)
      self.__fichero.write("\n")