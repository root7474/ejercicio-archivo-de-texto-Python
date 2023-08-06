import os
from Modules.CrearCarpeta import CrearCarpeta

class CrearArchivos(CrearCarpeta):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__opcion = None
        
    def getOpcion(self):
        return self.__opcion
    
    def crearArchivo(self):
        condicion = False
        print(os.getcwd())
        
        listado = os.listdir()
        for carpeta in listado: print(carpeta)
        
        while condicion == False:
            self.__opcion = self.optionError("Digita 1 para continuar, 0 para volver atrás: ")
        
            if self.getOpcion() == 1:
                ruta = self.filesErrors("Digita la ruta donde quieres que se ubique el archivo: ")
                os.chdir(ruta)
                self.setRuta
                
                listado = os.listdir()
                print(f"{self.getNombre()} digita el nombre de una carpeta para crear el archivo:\n")
                
                for carpeta in listado: print(carpeta)
                self.ruta = self.filesErrors("\nCarpeta: ")
            elif self.getOpcion() == 0:
                os.chdir("../")
                condicion = True
            else:
                print("Error!!!... Opción incorrecta")
                