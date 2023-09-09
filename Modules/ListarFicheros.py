import os
from Modules.Root import Root

class ListarFicheros(Root):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def listarFicheros(self):
        print(f"{self.getNombre()} qué carpeta deseas listar?:\n")
        lista = os.listdir("./")
        for i in lista: print(i)
        
        ruta = self.fileNotFound("\nOpción: ")
        self.setRuta(ruta)
        
        lista = os.listdir()
        for i in lista: print(i)

        separador = os.path.sep
        dirActual = os.path.dirname(os.path.abspath(__file__))
        
        self.setSeparador(separador)
        self.setDirActual(dirActual)
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1])
        self.setDirRaiz(dirRaiz)
        os.chdir(self.getDirRaiz())
