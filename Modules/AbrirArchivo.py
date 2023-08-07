import os
from Modules.CrearArchivos import CrearArchivos

class AbrirArchivo(CrearArchivos):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def abrirArchivo(self):
        # Continuar con esta función
        self.fileNotFound("Digita una ruta para crear el archivo: ")
        
        archivo = open(f"{self.getNombreArchivo()}", 'r')
        lecturaArchivo = archivo.read()
        
        print(lecturaArchivo)
        archivo.close()
        
        separador = os.path.sep
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        dir_raiz = separador.join(dir_actual.split(separador)[:-1])
        
        os.chdir(dir_raiz)
    