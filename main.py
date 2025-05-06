from interfaz.funciones_menu import Menu

if __name__ == "__main__":
    nombre_usuario = input("Ingrese su nombre: ")
    menu = Menu(nombre_usuario)
    menu.ejecutar()