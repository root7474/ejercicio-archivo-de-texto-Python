import os
from Modules.Root import Root

class RenombrarFicheros(Root):
    def __init__(self, nombre):
        super().__init__(nombre)

    def renombrarFichero(self):
        self.fileNotFound("Digita la ruta del fichero que deseas renombrar: ")
        lista = os.listdir()
        condicion = False

        while condicion == False:
            print("Qué fichero deseas renombrar?:\n")

            try:
                for i in lista: print(i)
                nombreFichero = input("\nOpción: ")
                ficheroNuevoNombre = input("Digita el nombre nuevo del fichero: ")

                os.rename(nombreFichero, ficheroNuevoNombre)
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
