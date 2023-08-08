import os
from Modules.CrearCarpeta import CrearCarpeta

class CrearArchivos(CrearCarpeta):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__nombreArchivo = None
    
    def setNombreArchivo(self, nombre):
        self.__nombreArchivo = nombre
    
    def getNombreArchivo(self):
        return self.__nombreArchivo
    
    def crearArchivo(self):
        self.fileNotFound("Digita una ruta para crear el archivo: ")
        self.__nombreArchivo = self.duplicateArchive(f"{self.getNombre()} digita el nombre del archivo a crear: ")
        
        separador = os.path.sep
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        dir_raiz = separador.join(dir_actual.split(separador)[:-1])
        
        os.chdir(dir_raiz)
    
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
    