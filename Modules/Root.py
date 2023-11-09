import os # Importamos al módulo "os"

"""
Clase "Root()" que permite controlar las excepciones que surjan durante la ejecución del programa.
Esta clase contiene las siguientes propiedades:
    - 6 atributos privados
    - Un constructor que inicializa los atributos privados en None (null)
    - Métodos set que reciben los valores de cada atributo
    - Métodos get que devuelven los valores de cada atributo
    - Funciones que controlan cada una de las excepciones en tiempo de ejecución y también retornan los datos ingresados por el usuario
"""
class Root:
    # Creamos un constructor para esta clase y le pasamos como parámetro "self"
    def __init__(self):
        # Creamos unos atributos privados y les pasamos un valor nulo (None)
        self.__nombre = None
        self.__ruta = None
        self.__nombreArchivo = None
        self.__separador = None
        self.__dirActual = None
        self.__dirRaiz = None

    # Definimos los métodos set con sus respectivos parámetros
    def setNombre(self, nombre):
        self.__nombre = nombre # "__nombre" recibe el valor del parámetro "nombre" de este método
    def setRuta(self, ruta):
        self.__ruta = ruta # "__ruta" recibe el valor del parámetro "ruta" de este método
    def setNombreArchivo(self, nombre):
        self.__nombreArchivo = nombre # "__nombreArchivo" recibe el valor del parámetro "nombre" de este método
    def setSeparador(self, separador):
        self.__separador = separador # "__separador" recibe el valor del parámetro "separador" de este método
    def setDirActual(self, dirActual):
        self.__dirActual = dirActual # "__dirActual" recibe el valor del parámetro "dirActual" de este método
    def setDirRaiz(self, dirRaiz):
        self.__dirRaiz = dirRaiz # "__dirRaiz" recibe el valor del parámetro "dirRaiz" de este método

    # Definimos los métodos get con su respectivo parámetro "self"
    def getNombre(self):
        return self.__nombre # Retornamos el valor de "__nombre"
    def getRuta(self):
        return self.__ruta # Retornamos el valor de "__ruta"
    def getNombreArchivo(self):
        return self.__nombreArchivo # Retornamos el valor de "__nombreArchivo"
    def getSeparador(self):
        return self.__separador # Retornamos el valor de "__separador"
    def getDirActual(self):
        return self.__dirActual # Retornamos el valor de "__dirActual"
    def getDirRaiz(self):
        return self.__dirRaiz # Retornamos el valor de "__dirRaiz"

    """
    Declaramos una función "fileNotFound()" que nos permite saber si se ha encontrado o no la ruta ingresada.
    Esta función contiene lo siguiente:
        - Dos parámetros "self" y "message" que recibe una cadena de caracteres
        - Una variable "dataUser" que imprime el valor del parámetro "message" y recibe los datos que ingrese el usuario
        - Una variable "condicion" que nos servirá como condicional del bucle "while" de esta función
    """
    def fileNotFound(self, message):
        dataUser = None # Inicializamos a dataUser con un valor nulo (None)
        condicion = False # Inicializamos a "condicion" en False

        # Mientras que "condicion" sea igual a False, haremos lo siguiente:
        while condicion == False:
            dataUser = input(message) # Imprimimos el valor de "message" y guardamos los datos que ingrese el usuario dentro de "dataUser"

            # Generamos un bloque try por si la ejecución del código es correcta
            # o no. En caso de que la ejecución del código no sea correcta,
            # se lanza un error de FileNotFoundError si la ruta no existe
            # o NotADirectoryError si el nombre ingresado no es un directorio
            try:
                self.setRuta(dataUser) # Enviamos la ruta ingresada por el usuario al método "setRuta()"
                os.chdir(self.getRuta()) # Mediante la función "chdir()" nos dirigimos a la ruta ingresada por el usuario
                print(f"\nEstás en: {os.getcwd()}") # Imprimimos la ruta en la que estamos
                condicion = True # A "condicion" le pasamos el valor de True y finalizamos la ejecución del ciclo
            except FileNotFoundError:
                print("Error!!!... El nombre de la carpeta o del archivo no existe") # Lanzamos esta excepción si no se ha encontrado la ruta ingresada
            except NotADirectoryError:
                print(f"Error!!!... El archivo: {self.getRuta()} no es un directorio") # Lanzamos esta excepción si el nombre ingresado es un archivo y no un directorio
        return dataUser # Devolvemos el valor de "dataUser"

    """
    Declaramos una función "fileExists()" que nos permite saber la existencia de un directorio.
    Esta función contiene lo siguiente:
        - Dos parámetros "self" y "message" que recibe una cadena de caracteres
        - Una variable "dataUser" que imprime el valor del parámetro "message" y recibe los datos que ingrese el usuario
        - Una variable "condicion" que nos servirá como condicional  del bucle "while" de esta función
    """
    def fileExists(self, message):
        dataUser = None # Inicializamos a "dataUser" con un valor nulo (None)
        condicion = False # Inicializamos a "condicion" en False

        # Mientras que "condicion" sea igual a False, haremos lo siguiente:
        while condicion == False:
            dataUser = input(message) # Imprimimos el valor de "message" y guardamos los datos que ingrese el usuario dentro de "dataUser"

            # Generamos un bloque try por si la ejecución del código es correcta
            # o no. En caso de que la ejecución del código no sea correcta,
            # se lanza un error de FileExistsError si existe el directorio
            try:
                os.makedirs(dataUser) # Si el el directorio no existe, lo creamos
                condicion = True # A "condicion" le pasamos el valor de True y finalizamos la ejecución del ciclo
            except FileExistsError:
                print("Error!!!... El archivo o carpeta ya existe") # Lanzamos esta excepción si el directorio ya existe
        return dataUser # Devolvemos el valor de "dataUser"

    """
    Declaramos una función "duplicateArchive()" que nos permite saber la existencia de un archivo.
    Esta función contiene lo siguiente:
        - Dos parámetros "self" y "message" que recibe una cadena de caracteres
        - Una variable "dataUser" que imprime el valor del parámetro "message" y recibe los datos que ingrese el usuario
        - Una variable "condicion" que nos servirá como condicional  del bucle "while" de esta función
        - Una variable "archivo" que nos permite abrir un archivo y retornarlo como un objeto
    """
    def duplicateArchive(self, message):
        dataUser = None # Inicializamos a "dataUser" con un valor nulo (None)
        condicion = False # Inicializamos a "condicion" en False

        # Mientras que "condicion" sea igual a False, haremos lo siguiente:
        while condicion == False:
            dataUser = input(message) # Imprimimos el valor de "message" y guardamos los datos que ingrese el usuario dentro de "dataUser"
            self.setNombreArchivo(dataUser) # Agregamos a la ruta el nombre del archivo y enviamos el resultado al método "setNombreArchivo()"
            
            if os.path.exists(self.getNombreArchivo()) == True:
                print("Error!!!... El archivo o carpeta ya existe") # Si el el nombre del archivo ingresado existe dentro de la ruta, lanzamos este error
            else:
                archivo = open(f"{self.getNombreArchivo()}", 'w') # Llamamos a la función "open()" y le pasamos como parámetros el nombre del archivo a crear y el permiso de escritura
                archivo.write(input()) # Hacemos que el usuario escriba algún texto con la función "write()", pasándole como parámetro de entrada la función "input()"
                archivo.close() # Mediante la función "close()" cerramos la ejecución ciclica de la función "open()"
                condicion = True # A "condicion" le pasamos el valor de True y finalizamos la ejecución del ciclo
        return dataUser # Devolvemos el valor de "dataUser"

    """
    Declaramos una función "optionError()" que nos permite evaluar las opciones ingresadas por el usuario dentro del menú de opciones de la clase "Menu()".
    Esta función contiene lo siguiente:
        - Dos parámetros "self" y "message" que recibe una cadena de caracteres
        - Una variable "dataUser" que imprime el valor del parámetro "message" y recibe los datos que ingrese el usuario
        - Una variable "condicion" que nos servirá como condicional  del bucle "while" de esta función
    """
    def optionError(self, message):
        dataUser = 0 # Inicializamos a "dataUser" en cero
        condicion = False # Inicializamos a "condicion" en False

        # Mientras que "condicion" sea igual a False, haremos lo siguiente:
        while condicion == False:
            try:
                dataUser = int(input(message)) # Imprimimos el valor de message y convertimos el dato ingresado a enteros dentro de "dataUser" y guardamos su resultado dentro de "dataUser"
                condicion = True # A "condicion" le pasamos el valor de True y finalizamos la ejecución del ciclo
            except ValueError:
                print("Error!!!... Solo debes ingresar números") # Generamos una excepción de tipo "ValueError" si la opción ingresada no es un número entero
        return dataUser # Devolvemos el valor de "dataUser"

    """
    Declaramos una función "noneError()" que nos permite evaluar el nombre ingresado por el usuario.
    Esta función contiene lo siguiente:
        - Dos parámetros "self" y "message" que recibe una cadena de caracteres
        - Una variable "condicion" que nos servirá como condicional  del bucle "while" de esta función
        - Una variable "nombre" que imprime el valor del parámetro "message" y recibe el nombre que ingrese el usuario
    """
    def noneError(self, message):
        condicion = False # Inicializamos a "condicion" en False
        nombre = "" # Inicializamos a "nombre" con un valor vacío

        while condicion == False:
            nombre = input(message) # Imprimimos el valor de message y guardamos los datos que ingrese el usuario dentro de "nombre"

            if nombre == "":
                print("Error!!!... Debes digitar tu nombre") # Si el valor de "nombre" es vacío (no ha sido ingresado), ejecutamos este mensaje de error
            else:
                condicion = True # Si el usuario ha ingresado algún nombre, a "condicion" le pasamos el valor de True y finalizamos la ejecución del ciclo
        return nombre # Devolvemos el valor de "nombre"