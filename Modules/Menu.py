import os

class Menu:
    __nombre = None
    
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def menu(self):
        condicion = False
        
        from Modules.CrearFicheros import CrearFicheros
        from Modules.LeerArchivo import LeerArchivo
        from Modules.EditarArchivos import EditarArchivos
        from Modules.ListarCarpetas import ListarCarpetas
        
        crearFicheros = CrearFicheros(self.getNombre())
        leerArchivo = LeerArchivo(self.getNombre())
        editarArchivos = EditarArchivos(self.getNombre())
        listarCarpetas = ListarCarpetas(self.getNombre())
        
        while condicion == False:
            print(f"\nEstás en: {os.getcwd()}")
            
            opcion = self.optionError(f"{self.getNombre()} digita una opción:\n"
                                      "\n1.) Crear carpetas o archivos."
                                      "\n2.) Listar carpetas."
                                      "\n3.) Leer archivos."
                                      "\n4.) Editar archivos."
                                      "\n5.) Renombrar archivos o carpetas."
                                      "\n6.) Eliminar carpetas o archivos."
                                      "\n0.) Salir."
                                      "\n\nOpción: ")
            
            match opcion:
                case 1:
                    opcion = self.optionError(f"{self.getNombre()} qué deseas hacer?:\n"
                                     "\n1.) Crear carpetas."
                                     "\n2.) Crear archivos.")
                    if opcion == 1:
                        crearFicheros.crearCarpeta()
                    elif opcion == 2:
                        crearFicheros.crearArchivo()
                    else:
                        print("Error!!!... Opción incorrecta")
                case 2:
                    listarCarpetas.listarCarpetas()
                case 3:
                    leerArchivo.leerArchivo()
                case 4:
                    editarArchivos.editarArchivo()
                case 5:
                    pass
                case 0:
                    print("Hasta pronto...")
                    condicion = True
                case default:
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
