import tkinter as tk
from tkinter import messagebox
import re

class Usuario:
    def __init__(self, nombre_completo, correo):
        self.nombre_completo = nombre_completo
        self.correo = correo

    def obtener_primer_nombre(self):
        return self.nombre_completo.strip().split()[0].capitalize()

    @staticmethod
    def verificar_correo(correo):
        patron = r"[^@]+@[^@]+\.[^@]+"
        return re.match(patron, correo) is not None

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


COLOR_FONDO = "#F5F8FA"
COLOR_TITULO = "#1E3A76"
COLOR_ENTRADA = "#A8D6E6"
COLOR_BOTON = "#3F5C92"
COLOR_BOTON_TEXTO = "#FFFFFF"

class LoginVentana:
    def __init__(self, master, sistema_autenticacion):
        self.master = master
        self.sistema = sistema_autenticacion

        master.title("Login - Asistente Virtual TechAsistant")
        master.geometry("400x300")
        master.configure(bg=COLOR_FONDO)

        # Título
        self.titulo = tk.Label(master, text="Bienvenido a TechAsistant", font=("Helvetica", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.titulo.pack(pady=20)

        # Nombre
        self.label_nombre = tk.Label(master, text="Nombre completo", bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master, bg=COLOR_ENTRADA, fg="black", width=30)
        self.entry_nombre.pack(pady=5)

        # Correo
        self.label_correo = tk.Label(master, text="Correo electrónico", bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.label_correo.pack()
        self.entry_correo = tk.Entry(master, bg=COLOR_ENTRADA, fg="black", width=30)
        self.entry_correo.pack(pady=5)

        # Botón de login/registro
        self.boton_login = tk.Button(master, text="Entrar", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                                     width=20, command=self.procesar_login)
        self.boton_login.pack(pady=20)

    def procesar_login(self):
        nombre = self.entry_nombre.get().strip()
        correo = self.entry_correo.get().strip()

        if not nombre or not correo:
            messagebox.showwarning("Campos requeridos", "Por favor, completa ambos campos.")
            return

        usuario, mensaje = self.sistema.registrar_o_login(nombre, correo)

        if usuario:
            messagebox.showinfo("Bienvenido", mensaje)
            # Aquí puedes continuar con el asistente por voz o abrir otro menú
            print("Usuario autenticado:", usuario.nombre_completo, usuario.correo)
        else:
            messagebox.showerror("Error", mensaje)


if __name__ == "__main__":
    root = tk.Tk()
    sistema = SistemaAutenticacion()
    app = LoginVentana(root, sistema)
    root.mainloop()


