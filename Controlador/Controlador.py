from Modelo.Modelo import Modelo
from Vista.VistaConsola import VistaConsola
from Vista.VistaFichero import VistaFichero 

class Controlador:
  def __init__ (self,nombreFichero):
    self.__modelo= Modelo()
    self.__fichero= VistaFichero(nombreFichero)
    self.__consola= VistaConsola()

  def leerLinea (self,mensaje):
    linea= self.__consola.leerLinea(mensaje)
    self.__modelo.agregarMensaje(linea)

  def escribirLineas (self):
    self.__fichero.abrir()
    self.__fichero.escribirLineas(self.__modelo.getListaMensajes())
    self.__fichero.cerrar()