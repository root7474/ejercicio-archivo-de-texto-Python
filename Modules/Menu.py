import os
from Modules.Root import Root

class Menu(Root):
    __nombre = None
    
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def getNombre(self):
        return super().getNombre()
    
    def menu(self):
        condicion = False
        
        from Modules.CrearFicheros import CrearFicheros
        from Modules.LeerArchivo import LeerArchivo
        from Modules.EditarArchivos import EditarArchivos
        from Modules.ListarFicheros import ListarFicheros
        from Modules.RenombrarFicheros import RenombrarFicheros
        
        crearFicheros = CrearFicheros(self.getNombre())
        listarFicheros = ListarFicheros(self.getNombre())
        leerArchivo = LeerArchivo(self.getNombre())
        editarArchivos = EditarArchivos(self.getNombre())
        renombrarFicheros = RenombrarFicheros(self.getNombre())
        
        while condicion == False:
            print(f"\nEstás en: {os.getcwd()}")
            
            opcion = self.optionError(f"{self.getNombre()} digita una opción:\n"
                                      "\n1.) Crear ficheros."
                                      "\n2.) Listar ficheros."
                                      "\n3.) Leer archivos."
                                      "\n4.) Editar archivos."
                                      "\n5.) Renombrar ficheros."
                                      "\n6.) Eliminar ficheros."
                                      "\n0.) Salir."
                                      "\n\nOpción: ")
            
            match opcion:
                case 1:
                    opcion = self.optionError(f"{self.getNombre()} qué deseas hacer?:\n"
                                              "\n1.) Crear carpetas."
                                              "\n2.) Crear archivos."
                                              "\n\nopción: ")
                    if opcion == 1:
                        crearFicheros.crearCarpeta()
                    elif opcion == 2:
                        crearFicheros.crearArchivo()
                    else:
                        print("Error!!!... Opción incorrecta")
                case 2:
                    listarFicheros.listarFicheros()
                case 3:
                    leerArchivo.leerArchivo()
                case 4:
                    editarArchivos.editarArchivo()
                case 5:
                    renombrarFicheros.renombrarFichero()
                case 6:
                    pass
                case 0:
                    print("Hasta pronto...")
                    condicion = True
                case default:
                    print("Error!!!... Opción incorrecta")
