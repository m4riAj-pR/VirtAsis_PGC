import tkinter as tk
from interfaz.login_usuario import SistemaAutenticacion, LoginVentana
from interfaz.Interfaz_menu import InterfazMenu

def lanzar_interfaz(usuario):
    interfaz = InterfazMenu(usuario)
    interfaz.mostrar_interfaz()

def main():
    sistema = SistemaAutenticacion()

    root = tk.Tk()
    root.withdraw()


    login_ventana = tk.Toplevel(root)
    app_login = LoginVentana(login_ventana, sistema)

    
    login_ventana.wait_window()


    if app_login.entry_nombre.get().strip() and app_login.entry_apellido.get().strip():
        usuario = f"{app_login.entry_nombre.get().strip()} {app_login.entry_apellido.get().strip()}".title()
        lanzar_interfaz(usuario)

if __name__ == "__main__":
    main()
