from Modules.Root import Root # Importamos a la clase "Root()" del módulo "Root.py"

"""
Clase "Menu()" que permite generar un menú de opciones. Esta clase hereda las propiedades del clase "Root()" y también contiene:
    - Un constructor que hereda del constructor de la superclase o clase padre
    - Una función "menu()" que genera el menú de opciones para el usuario
"""
class Menu(Root):
    # Creamos un constructor para esta clase y le pasamos como parámetro "self"
    def __init__(self):
        super().__init__() # Heredamos los atributos del constructor de la superclase "Root()"

    """
    Función "menu()". Esta función contiene lo siguiente:
        - Un parámetro "self" que permite la llamada a funciones, atributos y métodos
        - Una variable "condicion" que nos servirá como condicional del bucle "while" de esta función
        - Seis instancias de las clases a usar
        - Una variable "opcion" que imprime un menú de opciones
    """
    def menu(self):
        condicion = False # Inicializamos a "condicion" en False

        # Importamos las clases a usar
        from Modules.CrearFicheros import CrearFicheros
        from Modules.LeerArchivo import LeerArchivo
        from Modules.EditarArchivos import EditarArchivos
        from Modules.ListarFicheros import ListarFicheros
        from Modules.RenombrarFicheros import RenombrarFicheros
        from Modules.EliminarFicheros import EliminarFicheros

        # Creamos la instancia de dichas clases
        crearFicheros = CrearFicheros()
        listarFicheros = ListarFicheros()
        leerArchivo = LeerArchivo()
        editarArchivos = EditarArchivos()
        renombrarFicheros = RenombrarFicheros()
        eliminarFicheros = EliminarFicheros()

        # Mientras que "condicion" sea igual a False, haremos lo siguiente:
        while condicion == False:
            # Llamamos a la función "optionError()" de la clase "Root()" y le pasamos como string un menú de opciones
            opcion = self.optionError(f"{self.getNombre()} digita una opción:\n"
                                      "\n1.) Crear ficheros."
                                      "\n2.) Listar ficheros."
                                      "\n3.) Leer archivos."
                                      "\n4.) Editar archivos."
                                      "\n5.) Renombrar ficheros."
                                      "\n6.) Eliminar ficheros."
                                      "\n0.) Salir."
                                      "\n\nOpción: ") # Guardamos el valor que retorne la función dentro de la variable "opcion"

            # Generamos un match de la varible "opcion" para evaluar los casos de las opciones que elija el usuario
            match opcion:
                case 1:
                    # Para el caso 1, creamos un bucle while en el que volvemos generar un menú de opciones dentro de la variable "opcion"
                    while True:
                        opcion = self.optionError(f"{self.getNombre()} qué deseas hacer?:\n"
                                                  "\n1.) Crear carpetas."
                                                  "\n2.) Crear archivos."
                                                  "\n\nOpción: ") # Le pasamos otro string a la función "optionError()"
                        if opcion == 1:
                            crearFicheros.crearCarpeta() # Si "opcion" es igual a 1, llamamos a la función "crearCarpeta()" de la clase "CrearFicheros()"
                            break # Finalizamos la ejecución del bucle
                        elif opcion == 2:
                            crearFicheros.crearArchivo() # Si "opcion" es igual a 2, llamamos a la función "crearArchivo()" de la clase "CrearFicheros()"
                            break # Finalizamos la ejecución del bucle
                        else:
                            print("Error!!!... Opción incorrecta") # Si se digita una opción incorrecta, lanzamos un mensaje de error
                case 2:
                    listarFicheros.listarFicheros() # Para el caso 2, llamamos a la función "listarFicheros()" de la clase "ListarFicheros()"
                case 3:
                    leerArchivo.leerArchivo() # Para el caso 3, llamamos a la función "leerArchivo()" de la clase "LeerArchivo()"
                case 4:
                    editarArchivos.editarArchivo() # Para el caso 4, llamamos a la función "editarArchivo()" de la clase "EditarArchivo()"
                case 5:
                    renombrarFicheros.renombrarFichero() # Para el caso 5, llamamos a la función "renombrarFichero()" de la clase "RenombrarFicheros()"
                case 6:
                    eliminarFicheros.eliminarFicheros() # Para el caso 6, llamamos a la función "eliminarFicheros()" de la clase "EliminarFicheros()"
                case 0:
                    # Para el caso 6, "condicion" será igual a True y finalizamos la ejecución del programa
                    print("Hasta pronto...")
                    condicion = True
                case default:
                    print("Error!!!... Opción incorrecta") # Si no se digita una opción correcta, generamos un caso por defecto y lanzamos un mensaje de error
