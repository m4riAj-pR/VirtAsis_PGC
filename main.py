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

    usuario_logueado = app_login.obtener_usuario_logueado()

    if usuario_logueado:
        lanzar_interfaz(usuario_logueado)

if __name__ == "__main__":
    main()