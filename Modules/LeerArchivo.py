import os # Importamos al módulo "os"
from Modules.Root import Root # Importamos a la clase "Root()" del módulo "Root.py"

"""
Clase "LeerArchivo()" que permite visualizar el contenido de un archivo.
Esta clase hereda las propiedades del clase "Root()" y también contiene:
    - Un constructor que hereda del constructor de la superclase o clase padre
    - Una función "leerArchivo()" para visualizar el contenido de los archivos
"""
class LeerArchivo(Root):
    # Creamos un constructor para esta clase y le pasamos como parámetro "self"
    def __init__(self):
        super().__init__() # Heredamos los atributos del constructor de la superclase "Root()"

    """
    Función "leerArchivo()". Esta función contiene lo siguiente:
        - Un parámetro "self" que permite la llamada a funciones, atributos y métodos
        - Una variable "lista" en la que guardaremos una lista de los ficheros del directorio en el que nos encontremos
        - Una variable "condicion" que nos servirá como condicional del bucle "while" de esta función
        - Una variable "nombreArchivo" en la que guardaremos el nombre del archivo a visualizar
        - Una variable "archivo" que nos permite abrir un archivo y retornarlo como un objeto
        - Una variable "separador" en la que generaremos un separador para la ruta actual
        - Una variable "dirActual" que permite guardar la ruta desde donde se carga un módulo Python
        . Una variable "dirRaiz" que nos permite redirigirnos al directorio raíz
    """
    def leerArchivo(self):
        self.fileNotFound("Digita la ruta del archivo que deseas leer: ") # Hacemos una llamada a la función "fileNotFound()" de la clase "Root()" y le pasamos un string como parámetro
        lista = os.listdir() # Esto nos permite generar una lista con los nombres de los ficheros del directorio actual
        condicion = False # Inicializamos a "condicion" en False

        # Mientras que "condicion" sea igual a False, haremos lo siguiente:
        while condicion == False:
            # Pedimos que se ingrese el nombre del archivo a leer
            print("Qué archivo deseas leer?:\n")
            for i in lista: print(i) # Con un bucle for imprimimos los elementos de la lista
            nombreArchivo = input("\nOpción: ") # Dentro de "nombreArchivo" guardamos el nombre del archivo ingresado por consola

            if nombreArchivo in lista:
                # Si el archivo está dentro de la lista
                self.setNombreArchivo(nombreArchivo) # Enviamos el nombre del archivo al método "setNombreArchivo()" de la clase "Root()"
                archivo = open(f"{self.getNombreArchivo()}", 'r') # Llamamos a la función "open()" y le pasamos como parámetros el nombre del archivo a leer y el permiso de lectura
                lecturaArchivo = archivo.read() # Guardamos el contenido del archivo dentro de "lecturaArchivo"

                print(lecturaArchivo) # Imprimimos el contenido del archivo
                archivo.close() # Mediante la función "close()" cerramos la ejecución ciclica de la función "open()"
                condicion = True # A "condicion" le pasamos el valor de True y finalizamos la ejecución del ciclo
            else:
                # Si el nombre del archivo no está dentro de la lista
                print("Error!!!... El nombre de la carpeta o del archivo no existe") # Lanzamos este error

        separador = os.path.sep # Generamos un separador para la ruta actual dentro de "separador"
        dirActual = os.path.dirname(os.path.abspath(__file__)) # Guardamos la ruta del módulo actual dentro de "dirActual"
        
        self.setSeparador(separador) # Enviamos el separador generado al método "setSeparador()" de la clase "Root()"
        self.setDirActual(dirActual) # Enviamos la ruta generada al método "setDirActual()" de la clase "Root()"
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1]) # Dentro de "dirRaiz" guardamos la ruta del directorio raíz del módulo actual
        self.setDirRaiz(dirRaiz) # Enviamos la ruta del directorio raíz al método "setDirRaiz()" de la clase "Root()"
        os.chdir(self.getDirRaiz()) # Esto nos permite redirigirnos al directorio raíz
    