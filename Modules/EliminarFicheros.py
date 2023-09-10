import os
from shutil import rmtree
from Modules.Root import Root

class EliminarFicheros(Root):
    def __init__(self):
        super().__init__()

    def eliminarFicheros(self):
        self.fileNotFound("Digita la ruta del fichero que deseas eliminar: ")
        lista = os.listdir()
        condicion = False

        while condicion == False:
            print("Qué fichero deseas eliminar?:\n")
            for i in lista: print(i)
            nombreFichero = input("\nOpción: ")

            if nombreFichero in lista and os.path.isfile(nombreFichero):
                os.remove(nombreFichero)
                condicion = True
            elif nombreFichero in lista and os.path.isdir(nombreFichero):
                rmtree(nombreFichero)
                condicion = True
            else:
                print(f"Error!!!... El fichero {nombreFichero} no existe")

        separador = os.path.sep
        dirActual = os.path.dirname(os.path.abspath(__file__))

        self.setSeparador(separador)
        self.setDirActual(dirActual)

        dirRaiz = self.getSeparador().join(self.getDirActual().split(self.getSeparador())[:-1])
        self.setDirRaiz(dirRaiz)
        os.chdir(self.getDirRaiz())
