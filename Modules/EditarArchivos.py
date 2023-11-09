import os # Importamos al módulo "os"
from Modules.Root import Root # Importamos a la clase "Root()" del módulo "Root.py"

"""
Clase "EditarArchivos()" que permite editar el contenido de un archivo agregando contenido.
Esta clase hereda las propiedades del clase "Root()" y también contiene las siguientes propiedades:
    - Un constructor que hereda del constructor de la superclase o clase padre
    - Una función "editarArchivo()" para la edición de archivos
"""
class EditarArchivos(Root):
    # Creamos un constructor para esta clase y le pasamos como parámetro "self"
    def __init__(self):
        super().__init__() # Heredamos los atributos del constructor de la superclase "Root()"

    """
    Función "editarArchivo()". Esta función contiene lo siguiente:
        - Un parámetro "self" que permite la llamada a funciones, atributos y métodos
        - Una variable "lista" en la que guardaremos una lista de los ficheros del directorio en el que nos encontremos
        - Una variable "condicion" que nos servirá como condicional del bucle "while" de esta función
        - Una variable "nombreArchivo" en la que guardaremos el nombre del archivo a editar
        - Una variable "archivo" que nos permite abrir un archivo y retornarlo como un objeto
    """
    def editarArchivo(self):
        self.fileNotFound("Digita la ruta del archivo que deseas editar: ") # Hacemos una llamada a la función "fileNotFound()" de la clase "Root()" y le pasamos un string como parámetro
        lista = os.listdir() # Esto nos permite generar una lista con los nombres de los ficheros del directorio actual
        condicion = False # Inicializamos a "condicion" en False

        # Mientras que "condicion" sea igual a False, haremos lo siguiente:
        while condicion == False:
            # Pedimos que se ingrese el nombre del archivo a editar
            print("Qué archivo deseas editar?:\n")
            for i in lista: print(i) # Con un bucle for imprimimos los elementos de la lista
            nombreArchivo = input("\nOpción: ") # Dentro de "nombreArchivo" guardamos el nombre del archivo ingresado por consola

            if nombreArchivo in lista:
                # Si el archivo está dentro de la lista
                self.setNombreArchivo(nombreArchivo) # Enviamos el nombre del archivo al método "setNombreArchivo()" de la clase "Root()"
                archivo = open(f"{self.getNombreArchivo()}", 'a') # Llamamos a la función "open()" y le pasamos como parámetros el nombre del archivo a editar y el caracter 'a' que genera permisos para todas las clases de usuarios del sistema operativo principal
                archivo.write(f"\n{input()}") # Hacemos que el usuario escriba algún texto con la función "write()", pasándole como parámetro de entrada la función "input()"

                archivo = open(f"{self.getNombreArchivo()}", 'r') # Volvemos a llamamar a la función "open()" y le pasamos como parámetros el nombre del archivo a editar y el permiso de lectura
                print(archivo.read()) # Imprimimos el contenido del archivo

                archivo.close() # Mediante la función "close()" cerramos la ejecución ciclica de la función "open()"
                condicion = True # A "condicion" le pasamos el valor de True y finalizamos la ejecución del ciclo
            else:
                # Si el nombre del archivo no está dentro de la lista
                print(f"Error!!!... El archivo {nombreArchivo} no existe") # Lanzamos este error

        separador = os.path.sep # Generamos un separador para la ruta actual dentro de "separador"
        dirActual = os.path.dirname(os.path.abspath(__file__)) # Guardamos la ruta del módulo actual dentro de "dirActual"
        
        self.setSeparador(separador) # Enviamos el separador generado al método "setSeparador()" de la clase "Root()"
        self.setDirActual(dirActual) # Enviamos la ruta generada al método "setDirActual()" de la clase "Root()"
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1]) # Dentro de "dirRaiz" guardamos la ruta del directorio raíz del módulo actual
        self.setDirRaiz(dirRaiz) # Enviamos la ruta del directorio raíz al método "setDirRaiz()" de la clase "Root()"
        os.chdir(self.getDirRaiz()) # Esto nos permite redirigirnos al directorio raíz
