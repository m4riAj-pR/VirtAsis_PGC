import tkinter as tk
from tkinter import messagebox
import re
from menu_principal import *
from menu_principal import Menu 

COLOR_FONDO = "#F5F8FA"
COLOR_TITULO = "#1E3A76"
COLOR_ENTRADA = "#A8D6E6"
COLOR_BOTON = "#3F5C92"
COLOR_BOTON_TEXTO = "#FFFFFF"

class Usuario:
    def __init__(self, nombre_completo, correo):
        self.nombre_completo = nombre_completo
        self.correo = correo

    @staticmethod
    def verificar_correo(correo):
        patron = r"[^@]+@[^@]+\.[^@]+"
        return re.match(patron, correo) is not None
    
    def obtener_primer_nombre(self):
        return self.nombre_completo.strip().split()[0].capitalize()

class SistemaAutenticacion:
    def __init__(self):
        self.usuarios = {}

    def registrar_o_login(self, nombre_completo, correo):
        nombre_usuario = nombre_completo.lower().strip()

        if not Usuario.verificar_correo(correo):
            return None, "Correo inválido. Intenta de nuevo."

        if nombre_usuario in self.usuarios:
            usuario = self.usuarios[nombre_usuario]
            return usuario, f"¡Bienvenido de nuevo, {usuario.obtener_primer_nombre()}!"
        else:
            nuevo_usuario = Usuario(nombre_completo, correo)
            self.usuarios[nombre_usuario] = nuevo_usuario
            return nuevo_usuario, f"Registro exitoso. ¡Bienvenido/a, {nuevo_usuario.obtener_primer_nombre()}!"

class LoginVentana:
    def __init__(self, master, sistema_autenticacion):
        self.master = master
        self.sistema = sistema_autenticacion

        master.title("Login - Asistente Organizador TechAsistant")
        master.geometry("400x300")
        master.configure(bg=COLOR_FONDO)

    
        self.titulo = tk.Label(master, text="Bienvenido a TechAsistant", font=("Helvetica", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.titulo.pack(pady=20)


        self.label_nombre = tk.Label(master, text="Nombre completo", bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master, bg=COLOR_ENTRADA, fg="black", width=30)
        self.entry_nombre.pack(pady=5)


        self.label_correo = tk.Label(master, text="Correo electrónico", bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.label_correo.pack()
        self.entry_correo = tk.Entry(master, bg=COLOR_ENTRADA, fg="black", width=30)
        self.entry_correo.pack(pady=5)

    
        self.boton_login = tk.Button(master, text="Entrar", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                                     width=20, command=self.procesar_login)
        self.boton_login.pack(pady=20)

    def procesar_login(self):
        nombre = self.entry_nombre.get().strip()
        correo = self.entry_correo.get().strip()
        usuario_menu = nombre.capitalize()

        if not nombre or not correo:
            messagebox.showwarning("Campos requeridos", "Por favor, completa ambos campos.")
            return

        usuario, mensaje = self.sistema.registrar_o_login(nombre, correo)

        if usuario:
            messagebox.showinfo("Bienvenido", mensaje)
            menu = Menu(usuario_menu)
            menu.mostrar_opciones()  
            menu.ejecutar()  
            print("Usuario autenticado:", usuario.nombre_completo, usuario.correo)
        else:
            messagebox.showerror("Error", mensaje)

    def registrar_o_login(self, nombre_completo, correo):
        clave_usuario = nombre_completo.strip().lower()

        if not Usuario.verificar_correo(correo):
            return None, "Correo electrónico inválido."

        if clave_usuario in self.usuarios:
            usuario = self.usuarios[clave_usuario]
            if usuario.correo == correo:
                return usuario, f"¡Hola de nuevo, {usuario.obtener_primer_nombre()}!"
                menu = Menu(usuario_menu)
                menu.mostrar_opciones()  # ← usuario es un objeto Usuario
                menu.ejecutar()  
            else:
                return None, "El correo no coincide con el registrado."

        nuevo_usuario = Usuario(nombre_completo, correo)
        self.usuarios[clave_usuario] = nuevo_usuario
        return nuevo_usuario, f"¡Registro exitoso! Bienvenido/a, {nuevo_usuario.obtener_primer_nombre()}."

def main():
    root = tk.Tk()
    sistema_autenticacion = SistemaAutenticacion()
    app = LoginVentana(root, sistema_autenticacion)
    root.mainloop()

if __name__ == "__main__":
    main()

    
