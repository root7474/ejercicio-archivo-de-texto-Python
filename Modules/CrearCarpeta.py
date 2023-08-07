import os
from Modules.Menu import Menu

class CrearCarpeta(Menu):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__ruta = None
    
    def getNombre(self):
        return super().getNombre()
    
    def setRuta(self, ruta):
        self.__ruta = ruta
    
    def getRuta(self):
        return self.__ruta
    
    def crearCarpeta(self):
        self.__ruta = self.fileNotFound("Digita una ruta para crear la carpeta: ")
        self.fileExists(f"{self.getNombre()} digita el nombre de la carpeta a crear: ")

        separador = os.path.sep
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        dir_raiz = separador.join(dir_actual.split(separador)[:-1])
        
        os.chdir(dir_raiz)
    
    def fileNotFound(self, message):
        dataUser = None
        condicion = False
        
        while condicion == False:
            dataUser = input(message)
            
            try:
                self.setRuta(dataUser)
                os.chdir(self.getRuta())
                print(f"\n{os.getcwd()}")
                condicion = True
            except FileNotFoundError:
                print("Error!!!... El nombre de la carpeta o del archivo no existe")
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
    