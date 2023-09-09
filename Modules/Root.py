import os

class Root:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__ruta = None
        self.__nombreArchivo = None
        self.__separador = None
        self.__dirActual = None
        self.__dirRaiz = None
    
    def setRuta(self, ruta):
        self.__ruta = ruta
    def setNombreArchivo(self, nombre):
        self.__nombreArchivo = nombre
    def setSeparador(self, separador):
        self.__separador = separador
    def setDirActual(self, dirActual):
        self.__dirActual = dirActual
    def setDirRaiz(self, dirRaiz):
        self.__dirRaiz = dirRaiz
    
    def getNombre(self):
        return self.__nombre
    def getRuta(self):
        return self.__ruta
    def getNombreArchivo(self):
        return self.__nombreArchivo
    def getSeparador(self):
        return self.__separador
    def getDirActual(self):
        return self.__dirActual
    def getDirRaiz(self):
        return self.__dirRaiz
    
    def fileNotFound(self, message):
        dataUser = None
        condicion = False
        
        while condicion == False:
            dataUser = input(message)
            
            try:
                self.setRuta(dataUser)
                os.chdir(self.getRuta())
                print(f"\nEstás en: {os.getcwd()}")
                condicion = True
            except FileNotFoundError:
                print("Error!!!... El nombre de la carpeta o del archivo no existe")
            except NotADirectoryError:
                print(f"Error!!!... El archivo: {self.getRuta()} no es un directorio")
        return dataUser
    
    def fileExists(self, message):
        dataUser = None
        condicion = False
        
        while condicion == False:
            dataUser = input(message)
            
            try:
                os.makedirs(dataUser)
                condicion = True
            except FileExistsError:
                print("Error!!!... El archivo o carpeta ya existe")
        return dataUser
    
    def duplicateArchive(self, message):
        dataUser = None
        condicion = False
        
        while condicion == False:
            dataUser = input(message)
            self.setNombreArchivo(dataUser)
            
            if os.path.exists(self.getNombreArchivo()) == True:
                print("Error!!!... El archivo o carpeta ya existe")
            else:
                archivo = open(f"{self.getNombreArchivo()}", 'w')
                archivo.write(input())
                archivo.close()
                condicion = True
        return dataUser

    def optionError(self, message):
        dataUser = 0
        condicion = False

        while condicion == False:
            try:
                dataUser = int(input(message))
                condicion = True
            except ValueError:
                print("Error!!!... Solo debes ingresar números")
        return dataUser
    