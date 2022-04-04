from Controlador.Controlador import Controlador

def aplicacion ():
  controlador= Controlador("Resultado.txt")
  controlador.leerLinea("Introduzca una línea:")
  controlador.leerLinea("Introduzca la segunda línea:")
  controlador.escribirLineas()
  