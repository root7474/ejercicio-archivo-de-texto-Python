import os
from Modules.Excepciones import Root

class CrearFicheros(Root):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def crearCarpeta(self):
        ruta = self.fileNotFound("Digita una ruta para crear la carpeta: ")
        self.setRuta(ruta)
        self.fileExists(f"{self.getNombre()} digita el nombre de la carpeta a crear: ")

        separador = os.path.sep
        dirActual = os.path.dirname(os.path.abspath(__file__))
        
        self.setSeparador(separador)
        self.setDirActual(dirActual)
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1])
        self.setDirRaiz(dirRaiz)
        os.chdir(self.getDirRaiz())
        
    def crearArchivo(self):
        self.fileNotFound("Digita una ruta para crear el archivo: ")
        nombreArchivo = self.duplicateArchive(f"{self.getNombre()} digita el nombre del archivo a crear: ")
        self.setNombreArchivo(nombreArchivo)
        
        separador = os.path.sep
        dirActual = os.path.dirname(os.path.abspath(__file__))
        
        self.setSeparador(separador)
        self.setDirActual(dirActual)
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1])
        self.setDirRaiz(dirRaiz)
        os.chdir(self.getDirRaiz())
