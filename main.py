from core_asistente import Asistente_virtual
from funcion_voz import escuchar
from datetime import datetime
asistente = Asistente_virtual()

class Menu:
    def __init__(self, nombre):
        self.nombre = nombre


    def mostrar_opcciones(self):
            print(f"Hola {self.nombre}, estas son las opciones disponibles:")   
            print("> Crear lección")
            print("> Agregar temática")
            print("> Agregar recordatorio")
            print("> Mostrar lecciones")
            print("> Buscar lección")
            print("Salir")

    def ejecutar (self):
        while True:
            self.mostrar_opcciones()
            opcion = escuchar()

            if opcion == "crear lección":
                self.crear_leccion()
            elif opcion == "agregar temática":
                self.agg_tematica()
            elif opcion == "agregar recordatorio":
                self.agg_recordatorio()
            elif opcion == "buscar lecciones":
                self.buscar_leccion()
            elif opcion == "salir":
                print (f"Hasta pronto{self.nombre}")
                break 
            else:
                print("Opción inválida intentelo nuevamente")

    def crear_leccion(self):
        print("¿Cual es el nombre de la lección?")
        nombre_leccion = escuchar()
        print("¿Cual es el horario de la lección?")
        horario_leccion = escuchar()
        asistente.crear_leccion(nombre_leccion, horario_leccion)
        print("Lección creada con éxito")

    def agg_tematica(self):
        print("¿Cual es el nombre de la temática?")
        nombre_tematica = escuchar()
        print("¿Cual es la descripción de la temática?")
        descripcion_tematica = escuchar()
        asistente.agg_tematica(nombre_tematica, descripcion_tematica)
        print("Temática agregada con éxito")

    def agg_recordatorio(self):
        print("¿Qué mensaje desea agregar como recordatorio?")
        mensaje_recordatorio = escuchar()
        print("¿En qué fecha desea establecer el recordatorio? (formato: año-mes-día)")
        fecha_recordatorio = escuchar()
        fecha_recordatorio = datetime.strptime(fecha_recordatorio, "%Y-%m-%d")
        asistente.agg_recordatorio(mensaje_recordatorio, fecha_recordatorio)
        print("Recordatorio agregado con éxito")

    def buscar_leccion(self):
        print("¿Qué lección desea buscar?")
        nombre_leccion = escuchar()
        leccion_encontrada = asistente.buscar_leccion(nombre_leccion)
        if leccion_encontrada:
            print(f"Lección encontrada: {leccion_encontrada}")
        else:
            print("No se encontró ninguna lección con ese nombre")

print ("Bienvenido al asistente virtual, ¿cual es su nombre?")
nombre_usuario = escuchar()
menu_principal = Menu(nombre_usuario)
menu_principal.mostrar_opcciones()
menu_principal.ejecutar()





