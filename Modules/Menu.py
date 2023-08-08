import os

class Menu:
    __nombre = None
    
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def menu(self):
        condicion = False
        
        from Modules.CrearCarpeta import CrearCarpeta
        from Modules.CrearArchivos import CrearArchivos
        from Modules.LeerArchivo import LeerArchivo
        
        crearCarpeta = CrearCarpeta(self.getNombre())
        crearArchivos = CrearArchivos(self.getNombre())
        leerArchivo = LeerArchivo(self.getNombre())
        
        while condicion == False:
            print(f"\nEstás en: {os.getcwd()}")
            
            opcion = self.optionError(f"{self.getNombre()} digita una opción:\n"
                                      "\n1.) Crear carpeta."
                                      "\n2.) Crear archivo."
                                      "\n3.) Abrir archivo."
                                      "\n0.) Salir."
                                      "\n\nOpción: ")
            
            if opcion == 1:
                crearCarpeta.crearCarpeta()
            elif opcion == 2:
                crearArchivos.crearArchivo()
            elif opcion == 3:
                leerArchivo.leerArchivo()
            elif opcion == 0:
                print("Hasta pronto...")
                condicion = True
            else:
                print("Error!!!... Opción incorrecta")
            
    def optionError(self, message):
        dataUser = 0
        condicion = False
        
        while condicion == False:
            try:
                dataUser = int(input(message))
                condicion = True
            except ValueError:
                print("Error!!!... Solo debes ingresar números")
        return dataUser
