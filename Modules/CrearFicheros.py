import os # Importamos al módulo "os"
from Modules.Root import Root # Importamos a la clase "Root()" del módulo "Root.py"

"""
Clase "CrearFicheros()" que permite la creación de ficheros. Esta clase hereda las propiedades del clase "Root()"
y también contiene las siguientes propiedades:
    - Un constructor que hereda del constructor de la superclase o clase padre
    - Una función "crearCarpeta()" para crear directorios dentro de una ruta
    - Una función "crearArchivo()" para crear archivos dentro de una ruta
"""
class CrearFicheros(Root):
    # Creamos un constructor para esta clase y le pasamos como parámetro "self"
    def __init__(self):
        super().__init__() # Heredamos los atributos del constructor de la superclase "Root()"

    """
    Función "crearCarpeta()". Esta función contiene lo siguiente:
        - Un parámetro "self" que permite la llamada a funciones, atributos y métodos
        - Una variable "ruta" en la que guardaremos la ruta del directorio a crear
        - Una variable "separador" en la que generaremos un separador para dicha ruta
        - Una variable "dirActual" que permite guardar la ruta desde donde se carga un módulo Python
        . Una variable "dirRaiz" que nos permite redirigirnos al directorio raíz
    """
    def crearCarpeta(self):
        ruta = self.fileNotFound("Digita una ruta para crear la carpeta: ") # Dentro de ruta hacemos una llamada a la función "fileNotFound()" de la clase "Root()" y le pasamos un string como parámetro
        self.setRuta(ruta) # Enviamos el valor que retorna la función "fileNotFound()" al método "setRuta()" de la clase "Root()"
        self.fileExists(f"Digita el nombre de la carpeta a crear: ") # Hacemos la llamada a la función "fileExists()" de la clase "Root()" para evaluar si existe o no el directorio a crear

        separador = os.path.sep # Generamos un separador para la ruta actual dentro de "separador"
        dirActual = os.path.dirname(os.path.abspath(__file__)) # Guardamos la ruta del módulo actual dentro de "dirActual"
        
        self.setSeparador(separador) # Enviamos el separador generado al método "setSeparador()" de la clase "Root()"
        self.setDirActual(dirActual) # Enviamos la ruta generada al método "setDirActual()" de la clase "Root()"
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1]) # Dentro de "dirRaiz" guardamos la ruta del directorio raíz del módulo actual
        self.setDirRaiz(dirRaiz) # Enviamos la ruta del directorio raíz al método "setDirRaiz()" de la clase "Root()"
        os.chdir(self.getDirRaiz()) # Esto nos permite redirigirnos al directorio raíz

    """
    Función "crearArchivo()". Esta función contiene lo siguiente:
        - Un parámetro "self" que permite la llamada a funciones, atributos y métodos
        - Una variable "nombreArchivo" en la que guardaremos el nombre del archivo a crear
        - Una variable "separador" en la que generaremos un separador para dicha ruta
        - Una variable "dirActual" que permite guardar la ruta desde donde se carga un módulo Python
        . Una variable "dirRaiz" que nos permite redirigirnos al directorio raíz
    """
    def crearArchivo(self):
        self.fileNotFound("Digita una ruta para crear el archivo: ") # Hacemos una llamada a la función "fileNotFound()" de la clase "Root()" y le pasamos un string como parámetro
        nombreArchivo = self.duplicateArchive(f"Digita el nombre del archivo a crear: ") # Dentro de "nombreArchivo" hacemos una llamada a la función "duplicateArchive()" de la clase "Root()" y le pasamos un string como parámetro
        self.setNombreArchivo(nombreArchivo) # Enviamos el valor que retorna la función "duplicateArchive()" al método "setNombreArchivo()" de la clase "Root()"
        
        separador = os.path.sep # Generamos un separador para la ruta actual dentro de "separador"
        dirActual = os.path.dirname(os.path.abspath(__file__)) # Guardamos la ruta del módulo actual dentro de "dirActual"
        
        self.setSeparador(separador) # Enviamos el separador generado al método "setSeparador()" de la clase "Root()"
        self.setDirActual(dirActual) # Enviamos la ruta generada al método "setDirActual()" de la clase "Root()"
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1]) # Dentro de "dirRaiz" guardamos la ruta directorio raíz del módulo actual
        self.setDirRaiz(dirRaiz) # Enviamos la ruta del directorio raíz al método "setDirRaiz()"
        os.chdir(self.getDirRaiz()) # Esto nos permite redirigirnos al directorio raíz
