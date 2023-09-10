import os
from Modules.Root import Root

class EditarArchivos(Root):
    def __init__(self):
        super().__init__()
    
    def editarArchivo(self):
        self.fileNotFound("Digita la ruta del archivo que deseas editar: ")
        lista = os.listdir()
        condicion = False
        
        while condicion == False:
            print("Qué archivo deseas editar?:\n")
            for i in lista: print(i)
            nombreArchivo = input("\nOpción: ")
            # filtrado = [archivo for archivo in lista if nombreArchivo == archivo]

            if nombreArchivo in lista:
                self.setNombreArchivo(nombreArchivo)
                archivo = open(f"{self.getNombreArchivo()}", 'a')
                archivo.write(f"\n{input()}")

                archivo = open(f"{self.getNombreArchivo()}", 'r')
                print(archivo.read())

                archivo.close()
                condicion = True
            else:
                print(f"Error!!!... El archivo {nombreArchivo} no existe")

        separador = os.path.sep
        dirActual = os.path.dirname(os.path.abspath(__file__))
        
        self.setSeparador(separador)
        self.setDirActual(dirActual)
        
        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1])
        self.setDirRaiz(dirRaiz)
        os.chdir(self.getDirRaiz())
