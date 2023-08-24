import os
from Modules.CrearCarpeta import CrearCarpeta

class ListarCarpetas(CrearCarpeta):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def listarCarpetas(self):
        print(f"{self.getNombre()} qué carpeta deseas listar?:\n")
        lista = os.listdir("./")
        for i in lista: print(i)
        
        ruta = self.fileNotFound("\nOpción: ")
        self.setRuta(ruta)
        
        lista = os.listdir()
        for i in lista: print(i)

        separador = os.path.sep
        self.setSeparador(separador)
        dirActual = os.path.dirname(os.path.abspath(__file__))
        self.setDirActual(dirActual)
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1])
        self.setDirRaiz(dirRaiz)
        
        os.chdir(self.getDirRaiz())
