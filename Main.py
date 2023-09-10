from Modules.Menu import Menu
from Modules.Root import Root

def main():
    root = Root()
    menu = Menu()

    try:
        nombre = root.noneError("Bienvenido... \nDigita tu nombre: ")
        menu.setNombre(nombre)
        menu.menu()
    except EOFError:
        print("Hasta pronto...")

if __name__ == "__main__":
    main()
