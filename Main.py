from Modules.Menu import Menu

def main():
    try:
        nombre = input("Bienvenido... \nDigita tu nombre: ")
        menu = Menu(nombre)
        menu.menu()
    except EOFError:
        print("Hasta pronto...")

if __name__ == "__main__":
    main()
