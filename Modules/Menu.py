import os
from Modules.Root import Root

class Menu(Root):
    def __init__(self):
        super().__init__()
    
    def menu(self):
        condicion = False
        
        from Modules.CrearFicheros import CrearFicheros
        from Modules.LeerArchivo import LeerArchivo
        from Modules.EditarArchivos import EditarArchivos
        from Modules.ListarFicheros import ListarFicheros
        from Modules.RenombrarFicheros import RenombrarFicheros
        from Modules.EliminarFicheros import EliminarFicheros
        
        crearFicheros = CrearFicheros()
        listarFicheros = ListarFicheros()
        leerArchivo = LeerArchivo()
        editarArchivos = EditarArchivos()
        renombrarFicheros = RenombrarFicheros()
        eliminarFicheros = EliminarFicheros()

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
                    while True:
                        opcion = self.optionError(f"{self.getNombre()} qué deseas hacer?:\n"
                                                  "\n1.) Crear carpetas."
                                                  "\n2.) Crear archivos."
                                                  "\n\nOpción: ")
                        if opcion == 1:
                            crearFicheros.crearCarpeta()
                            break
                        elif opcion == 2:
                            crearFicheros.crearArchivo()
                            break
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
                    eliminarFicheros.eliminarFicheros()
                case 0:
                    print("Hasta pronto...")
                    condicion = True
                case default:
                    print("Error!!!... Opción incorrecta")
