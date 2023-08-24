import os
from Modules.Root import Root

class LeerArchivo(Root):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def leerArchivo(self):
        self.fileNotFound("Digita la ruta del archivo que deseas leer: ")
        lista = os.listdir()
        condicion = False
        
        while condicion == False:
            print("Qué archivo deseas leer?:\n")
            
            try:
                for i in lista: print(i)
                nombreArchivo = input("\nOpción: ")
                
                self.setNombreArchivo(nombreArchivo)
                archivo = open(f"{self.getNombreArchivo()}", 'r')
                lecturaArchivo = archivo.read()
                
                print(lecturaArchivo)
                archivo.close()
                condicion = True
            except FileNotFoundError:
                print("Error!!!... El nombre de la carpeta o del archivo no existe")

        separador = os.path.sep
        dirActual = os.path.dirname(os.path.abspath(__file__))
        
        self.setSeparador(separador)
        self.setDirActual(dirActual)
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1])
        self.setDirRaiz(dirRaiz)
        os.chdir(self.getDirRaiz())
    