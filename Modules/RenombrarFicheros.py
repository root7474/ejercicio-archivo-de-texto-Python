import os # Importamos al módulo "os"
from Modules.Root import Root # Importamos a la clase "Root()" del módulo "Root.py"

"""
Clase "RenombrarFicheros()" que permite cambiar el nombre de un fichero.
Esta clase hereda las propiedades del clase "Root()" y también contiene:
    - Un constructor que hereda del constructor de la superclase o clase padre
    - Una función "renombrarFichero()" para renombrar ficheros
"""
class RenombrarFicheros(Root):
    # Creamos un constructor para esta clase y le pasamos como parámetro "self"
    def __init__(self):
        super().__init__() # Heredamos los atributos del constructor de la superclase "Root()"

    """
    Función "renombrarFichero()". Esta función contiene lo siguiente:
        - Un parámetro "self" que permite la llamada a funciones, atributos y métodos
        - Una variable "lista" en la que guardaremos una lista de los ficheros del directorio en el que nos encontremos
        - Una variable "condicion" que nos servirá como condicional del bucle "while" de esta función
        - Una variable "nombreFichero" en la que guardaremos el nombre antiguo del fichero a renombrar
        - Una variable "ficheroNuevoNombre" en la que guardaremos el nuevo nombre del fichero a renombrar
        - Una variable "separador" en la que generaremos un separador para la ruta actual
        - Una variable "dirActual" que permite guardar la ruta desde donde se carga un módulo Python
        . Una variable "dirRaiz" que nos permite redirigirnos al directorio raíz
    """
    def renombrarFichero(self):
        self.fileNotFound("Digita la ruta del fichero que deseas renombrar: ") # Hacemos una llamada a la función "fileNotFound()" de la clase "Root()" y le pasamos un string como parámetro
        lista = os.listdir() # Esto nos permite generar una lista con los nombres de los ficheros del directorio actual
        condicion = False # Inicializamos a "condicion" en False

        # Mientras que "condicion" sea igual a False, haremos lo siguiente:
        while condicion == False:
            # Pedimos que se ingrese el nombre del fichero a renombrar
            print("Qué fichero deseas renombrar?:\n")
            for i in lista: print(i) # Con un bucle for imprimimos los elementos de la lista
            nombreFichero = input("\nOpción: ") # Dentro de "nombreFichero" guardamos el nombre antiguo del fichero ingresado por consola

            if nombreFichero in lista:
                # Si el fichero está dentro de la lista
                ficheroNuevoNombre = input("Digita el nombre nuevo del fichero: ") # Dentro de "ficheroNuevoNombre" guardamos el nuevo nombre del fichero ingresado por consola
                os.rename(nombreFichero, ficheroNuevoNombre) # Esto nos permite intercambiar el nombre antiguo por el nombre nuevo que hemos generado por consola
                condicion = True # A "condicion" le pasamos el valor de True y finalizamos la ejecución del ciclo
            else:
                # Si el nombre del fichero no está dentro de la lista
                print(f"Error!!!... El fichero {nombreFichero} no existe") # Lanzamos este error

        separador = os.path.sep # Generamos un separador para la ruta actual dentro de "separador"
        dirActual = os.path.dirname(os.path.abspath(__file__)) # Guardamos la ruta del módulo actual dentro de "dirActual"

        self.setSeparador(separador) # Enviamos el separador generado al método "setSeparador()" de la clase "Root()"
        self.setDirActual(dirActual) # Enviamos la ruta generada al método "setDirActual()" de la clase "Root()"

        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1]) # Dentro de "dirRaiz" guardamos la ruta del directorio raíz del módulo actual
        self.setDirRaiz(dirRaiz) # Enviamos la ruta del directorio raíz al método "setDirRaiz()" de la clase "Root()"
        os.chdir(self.getDirRaiz()) # Esto nos permite redirigirnos al directorio raíz
