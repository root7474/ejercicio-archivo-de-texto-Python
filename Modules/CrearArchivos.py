import os
from Modules.CrearCarpeta import CrearCarpeta

class CrearArchivos(CrearCarpeta):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__nombreArchivo = None
        
    def getNombreArchivo(self):
        return self.__nombreArchivo
    
    def crearArchivo(self):
        self.fileNotFound("Digita una ruta para crear el archivo: ")
        self.__nombreArchivo = input(f"{self.getNombre()} digita el nombre del archivo a crear: ")
        archivo = open(f"{self.getNombreArchivo()}", 'w')
        
        archivo.write(input())
        archivo.close()
        
        separador = os.path.sep
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        dir_raiz = separador.join(dir_actual.split(separador)[:-1])
        
        os.chdir(dir_raiz)
    