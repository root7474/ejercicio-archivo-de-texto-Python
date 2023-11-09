import os # Importamos al módulo "os"
from shutil import rmtree # Importamos a la función "rmtree()" del módulo "shutil"
from Modules.Root import Root # Importamos a la clase "Root()" del módulo "Root.py"

"""
Clase "EliminarFicheros()" que permite eliminar un determinado fichero.
Esta clase hereda las propiedades del clase "Root()" y también contiene:
    - Un constructor que hereda del constructor de la superclase o clase padre
    - Una función "eliminarFicheros()" cuyo objetivo es eliminar ficheros
"""
class EliminarFicheros(Root):
    # Creamos un constructor para esta clase y le pasamos como parámetro "self"
    def __init__(self):
        super().__init__() # Heredamos los atributos del constructor de la superclase "Root()"

    """
    Función "eliminarFicheros()". Esta función contiene lo siguiente:
        - Un parámetro "self" que permite la llamada a funciones, atributos y métodos
        - Una variable "lista" en la que guardaremos una lista de los ficheros del directorio en el que nos encontremos
        - Una variable "condicion" que nos servirá como condicional del bucle "while" de esta función
        - Una variable "nombreFichero" en la que guardaremos el nombre del fichero a eliminar
        - Una variable "separador" en la que generaremos un separador para la ruta actual
        - Una variable "dirActual" que permite guardar la ruta desde donde se carga un módulo Python
        . Una variable "dirRaiz" que nos permite redirigirnos al directorio raíz
    """
    def eliminarFicheros(self):
        self.fileNotFound("Digita la ruta del fichero que deseas eliminar: ") # Hacemos una llamada a la función "fileNotFound()" de la clase "Root()" y le pasamos un string como parámetro
        lista = os.listdir() # Esto nos permite generar una lista con los nombres de los ficheros del directorio actual
        condicion = False # Inicializamos a "condicion" en False

        # Mientras que "condicion" sea igual a False, haremos lo siguiente:
        while condicion == False:
            # Pedimos que se ingrese el nombre del fichero a eliminar
            print("Qué fichero deseas eliminar?:\n")
            for i in lista: print(i) # Con un bucle for imprimimos los elementos de la lista
            nombreFichero = input("\nOpción: ") # Dentro de "nombreFichero" guardamos el nombre del fichero ingresado por consola

            if nombreFichero in lista and os.path.isfile(nombreFichero):
                # Si el fichero está dentro de la lista y además es un archivo
                os.remove(nombreFichero) # Esto nos permite remover o eliminar dicho archivo
                condicion = True # A "condicion" le pasamos el valor de True y finalizamos la ejecución del ciclo
            elif nombreFichero in lista and os.path.isdir(nombreFichero):
                # Si el fichero está dentro de la lista y además es un directorio
                rmtree(nombreFichero) # Esto nos permite remover o eliminar dicho directorio
                condicion = True # A "condicion" le volvemos a pasar el valor de True y finalizamos la ejecución del ciclo
            else:
                # Si el nombre del archivo o directorio no está dentro de la lista
                print(f"Error!!!... El fichero {nombreFichero} no existe") # Lanzamos este error

        separador = os.path.sep # Generamos un separador para la ruta actual dentro de "separador"
        dirActual = os.path.dirname(os.path.abspath(__file__)) # Guardamos la ruta del módulo actual dentro de "dirActual"

        self.setSeparador(separador) # Enviamos el separador generado al método "setSeparador()" de la clase "Root()"
        self.setDirActual(dirActual) # Enviamos la ruta generada al método "setDirActual()" de la clase "Root()"

        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1]) # Dentro de "dirRaiz" guardamos la ruta del directorio raíz del módulo actual
        self.setDirRaiz(dirRaiz) # Enviamos la ruta del directorio raíz al método "setDirRaiz()" de la clase "Root()"
        os.chdir(self.getDirRaiz()) # Esto nos permite redirigirnos al directorio raíz
