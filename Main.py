# Programa para crear, leer, editar y eliminar ficheros
# Autor: David Rodríguez
# Importamos las clases a usar
from Modules.Menu import Menu
from Modules.Root import Root

"""
Función "main()" que permite la ejecución del programa.
Esta función contiene:
    - Dos instancias delas clases que hemos importado
    - Una variable que permite la entrada de datos
    - Dos instancias de funciones que pertencen a las clases importadas
"""
def main():
    # Instanciamos a las clases que hemos importado
    root = Root()
    menu = Menu()

    # Generamos un bloque try por si la ejecución del código es correcta
    # o no. En caso de que la ejecución del código no sea correcta,
    # se lanza un error de EOFError.
    try:
        nombre = root.noneError("Bienvenido... \nDigita tu nombre: ") # Enviamos el nombre del usuario a la función "noneError()" de la clase "Root()" y guardamos el valor que devuelva la función dentro de la variable "nombre"
        menu.setNombre(nombre) # Enviamos el valor de "nombre" al método "setNombre()" de la clase "Menu()"
        menu.menu() # Instanciamos a la función "menu()" de la clase "Menu()"
    except EOFError:
        print("Hasta pronto...") # En este caso no imprmiremos un mensaje de error, solamente finalizamos la ejecución del programa

# Permitimos que se ejecute la función "main()"
if __name__ == "__main__":
    main()
