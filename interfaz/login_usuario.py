import tkinter as tk
from tkinter import messagebox
import re
import json

COLOR_FONDO = "#F5F8FA"
COLOR_TITULO = "#1E3A76"
COLOR_ENTRADA = "#A8D6E6"
COLOR_BOTON = "#3F5C92"
COLOR_BOTON_TEXTO = "#FFFFFF"
ARCHIVO_USUARIOS = "usuarios.json"

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

    def a_dict(self):
        return {"nombre_completo": self.nombre_completo, "correo": self.correo}

    @classmethod
    def desde_dict(cls, data):
        return cls(data["nombre_completo"], data["correo"])

    def __str__(self):
        return self.obtener_primer_nombre()

class SistemaAutenticacion:
    def __init__(self):
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        try:
            with open(ARCHIVO_USUARIOS, 'r') as f:
                data = json.load(f)
                return {nombre: Usuario.desde_dict(usuario_data) for nombre, usuario_data in data.items()}
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"Error al decodificar el archivo de usuarios ({ARCHIVO_USUARIOS}). Los usuarios se restablecerán.")
            return {}

    def guardar_usuarios(self):
        data = {nombre: usuario.a_dict() for nombre, usuario in self.usuarios.items()}
        try:
            with open(ARCHIVO_USUARIOS, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Usuarios guardados en {ARCHIVO_USUARIOS}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar los usuarios en {ARCHIVO_USUARIOS}:\n{e}")

    def registrar_o_login(self, nombre_completo, correo):
        clave_usuario = nombre_completo.lower().strip()

        if not Usuario.verificar_correo(correo):
            return None, "Correo electrónico inválido."

        if clave_usuario in self.usuarios:
            usuario = self.usuarios[clave_usuario]
            if usuario.correo == correo:
                return usuario, f"¡Hola de nuevo, {usuario.obtener_primer_nombre()}!"
            else:
                return None, "El correo no coincide con el registrado."
        else:
            nuevo_usuario = Usuario(nombre_completo, correo)
            self.usuarios[clave_usuario] = nuevo_usuario
            self.guardar_usuarios() 
            return nuevo_usuario, f"¡Registro exitoso! Bienvenido/a, {nuevo_usuario.obtener_primer_nombre()}."

class LoginVentana:
    def __init__(self, master, sistema_autenticacion):
        self.master = master
        self.sistema = sistema_autenticacion
        self.usuario_logueado = None
        self.entry_nombre_clicked = False
        self.entry_apellido_clicked = False
        self.entry_correo_clicked = False

        master.title("Login - Asistente Organizador TechAsistant")
        master.geometry("400x400")
        master.configure(bg=COLOR_FONDO)

        self.titulo = tk.Label(master, text="Bienvenido a TechAsistant", font=("Poppins", 16, "bold"),
                                    bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.titulo.pack(pady=20)

        self.label_nombre = tk.Label(master, text="Nombres", bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(master, bg=COLOR_ENTRADA, width=30)
        self.entry_nombre.insert(0, "Ingrese su nombre")
        self.entry_nombre.pack(pady=5)
        self.entry_nombre.bind("<FocusIn>", self.borrar_nombre)

        self.label_apellido = tk.Label(master, text="Apellidos", bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.label_apellido.pack()
        self.entry_apellido = tk.Entry(master, bg=COLOR_ENTRADA, width=30)
        self.entry_apellido.insert(0, "Ingrese su apellido")
        self.entry_apellido.pack(pady=5)
        self.entry_apellido.bind("<FocusIn>", self.borrar_apellido)

        self.label_correo = tk.Label(master, text="Correo electrónico", bg=COLOR_FONDO, fg=COLOR_TITULO)
        self.label_correo.pack()
        self.entry_correo = tk.Entry(master, bg=COLOR_ENTRADA, width=30)
        self.entry_correo.insert(0, "ejemplo@correo.com")
        self.entry_correo.pack(pady=5)
        self.entry_correo.bind("<FocusIn>", self.borrar_correo)

        self.boton_login = tk.Button(master, text="Entrar", bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                                        width=20, command=self.procesar_login)
        self.boton_login.pack(pady=20)

    def borrar_nombre(self, event):
        if not self.entry_nombre_clicked:
            self.entry_nombre.delete(0, 'end')
            self.entry_nombre_clicked = True

    def borrar_apellido(self, event):
        if not self.entry_apellido_clicked:
            self.entry_apellido.delete(0, 'end')
            self.entry_apellido_clicked = True

    def borrar_correo(self, event):
        if not self.entry_correo_clicked:
            self.entry_correo.delete(0, 'end')
            self.entry_correo_clicked = True

    def procesar_login(self):
        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        correo = self.entry_correo.get().strip()

        if not nombre or not apellido or not correo:
            messagebox.showwarning("Campos requeridos", "Por favor, completa todos los campos.")
            return

        nombre_completo = f"{nombre} {apellido}".title()
        usuario, mensaje = self.sistema.registrar_o_login(nombre_completo, correo)

        if usuario:
            messagebox.showinfo("Bienvenido", mensaje)
            self.usuario_logueado = usuario
            self.master.destroy()
        else:
            messagebox.showerror("Error", mensaje)

    def obtener_usuario_logueado(self):
        return self.usuario_logueado