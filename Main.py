from Modules.Menu import Menu

def main():
    nombre = input("Bienvenido... \nDigita tu nombre: ")
    menu = Menu(nombre)
    menu.menu()
    

if __name__ == "__main__":
    main()
