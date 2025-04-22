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

    def registrar_usuario(self):
        print(" Registro de usuario ")
        nombre_completo = input("Ingresa tu nombre completo (nombre y apellido): ").strip()
        correo = input("Ingresa tu correo electrónico: ").strip()

        if not Usuario.verificar_correo(correo):
            print("Correo inválido. Intenta de nuevo.")
            return None

        nombre_usuario = nombre_completo.lower()
        if nombre_usuario in self.usuarios:
            print("Este usuario ya está registrado.")
            return None

        self.usuarios[nombre_usuario] = Usuario(nombre_completo, correo)
        print(f"Registro exitoso. ¡Bienvenido/a, {nombre_completo}!")
        return self.usuarios[nombre_usuario]

    def iniciar_sesion(self):
        print(" Inicio de sesión ")
        nombre_completo = input("Ingresa tu nombre completo: ").strip().lower()
        if nombre_completo in self.usuarios:
            usuario = self.usuarios[nombre_completo]
            print(f"¡Hola de nuevo, {usuario.obtener_primer_nombre()}!")
            return usuario
        else:
            print("Usuario no encontrado. Por favor regístrate primero.")
            return None
