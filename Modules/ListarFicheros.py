import os # Importamos al módulo "os"
from Modules.Root import Root # Importamos a la clase "Root()" del módulo "Root.py"

"""
Clase "ListarFicheros()" que permite mostrar los ficheros de un directorio.
Esta clase hereda las propiedades del clase "Root()" y también contiene las siguientes propiedades:
    - Un constructor que hereda del constructor de la superclase o clase padre
    - Una función "listarFicheros()" para listar directorios dentro de una ruta
"""
class ListarFicheros(Root):
    # Creamos un constructor para esta clase y le pasamos como parámetro "self"
    def __init__(self):
        super().__init__() # Heredamos los atributos del constructor de la superclase "Root()"

    """
    Función "crearCarpeta()". Esta función contiene lo siguiente:
        - Un parámetro "self" que permite la llamada a funciones, atributos y métodos
        - Una variable "lista" en la que guardaremos una lista de los ficheros del directorio en el que nos encontremos
        - Una variable "ruta" en la que guardaremos la ruta del directorio a listar
        - Una variable "separador" en la que generaremos un separador para dicha ruta
        - Una variable "dirActual" que permite guardar la ruta desde donde se carga un módulo Python
        . Una variable "dirRaiz" que nos permite redirigirnos al directorio raíz
    """
    def listarFicheros(self):
        print(f"{self.getNombre()} qué carpeta deseas listar?:\n")
        lista = os.listdir("./") # Esto nos permite generar una lista con los nombres de los ficheros del directorio raíz
        for i in lista: print(i) # Con un bucle for imprimimos los elementos de la lista
        
        ruta = self.fileNotFound("\nOpción: ") # Dentro de ruta hacemos una llamda a la función "fileNotFound()" de la clase "Root()" y le pasamos un string como parámetro
        self.setRuta(ruta) # Enviamos el valor que retorna la función "fileNotFound()" al método "setRuta()" de la clase "Root()"
        
        lista = os.listdir() # Sobrescribimos a la variable "lista" y le pasamos como nuevo valor una lista del directorio en el que nos encontremos
        for i in lista: print(i) # Con un bucle for imprimimos los elementos de la nueva lista

        separador = os.path.sep # Generamos un separador para la ruta actual dentro de "separador"
        dirActual = os.path.dirname(os.path.abspath(__file__)) # Guardamos la ruta del módulo actual dentro de "dirActual"
        
        self.setSeparador(separador) # Enviamos el separador generado al método "setSeparador()" de la clase "Root()"
        self.setDirActual(dirActual) # Enviamos la ruta generada al método "setDirActual()" de la clase "Root()"
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1]) # Dentro de "dirRaiz" guardamos la ruta del directorio raíz del módulo actual
        self.setDirRaiz(dirRaiz) # Enviamos la ruta del directorio raíz al método "setDirRaiz()" de la clase "Root()"
        os.chdir(self.getDirRaiz()) # Esto nos permite redirigirnos al directorio raíz
