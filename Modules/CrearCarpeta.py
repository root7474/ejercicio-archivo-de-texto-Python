import os
from Modules.Menu import Menu

class CrearCarpeta(Menu):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.ruta = None
    
    def getNombre(self):
        return super().getNombre()
    
    def setRuta(self, ruta):
        self.ruta = ruta
    
    def getRuta(self):
        return self.ruta
    
    def crearCarpeta(self):
        condicion = False
        self.ruta = self.filesErrors("Digita una ruta para crear la carpeta: ")
        
        while condicion == False:
            try:
                os.makedirs(input(f"{self.getNombre()} digita el nombre de la carpeta a crear: "))
                condicion = True
            except FileExistsError:
                print("Error!!!... El nombre de la carpeta ya existe")
    
    def filesErrors(self, message):
        dataUser = None
        condicion = False
        
        while condicion == False:
            dataUser = input(f"{message}")
            
            try:
                self.setRuta(dataUser)
                os.chdir(self.getRuta())
                condicion = True
            except FileNotFoundError:
                print("Error!!!... El nombre de la carpeta o del archivo no existe")
        return dataUser
