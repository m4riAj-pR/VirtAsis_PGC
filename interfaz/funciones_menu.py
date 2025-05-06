from datetime import datetime
from core.asistente_virtual import AsistenteVirtual
from core.voz.voz_asistente import AsistenteDeVoz

asistente_organizador = AsistenteVirtual()
asistente_voz = AsistenteDeVoz()

class Menu:
    def __init__(self, usuario):
        self.usuario = usuario
        self.menu_desbloqueado = len(asistente_organizador.clases) > 0 # Desbloquear si ya hay clases guardadas

    def mostrar_opciones_iniciales(self):
        asistente_voz.hablar(f"Hola {self.usuario}, soy Zeta, tu asistente virtual.")
        asistente_voz.hablar("Estas son las opciones iniciales:")
        asistente_voz.hablar("""
1. Crear clase
2. Agregar recordatorio general
3. Salir
""")
        if asistente_organizador.clases:
            asistente_voz.hablar("Ya existen clases guardadas. Puedes acceder al menú completo.")
            asistente_voz.hablar("Escribe 'menu' para ver todas las opciones.")

    def mostrar_opciones_completas(self):
        asistente_voz.hablar("Estas son las opciones disponibles:")
        asistente_voz.hablar("""
1. Crear clase
2. Crear lección dentro de una clase
3. Agregar tarea a lección
4. Agregar recordatorio general
5. Mostrar recordatorios
6. Mostrar clases y lecciones
7. Guardar datos
8. Salir
""")

    def obtener_input_con_reintento(self, pregunta, es_fecha=False):
        while True:
            asistente_voz.hablar(pregunta)
            respuesta = asistente_voz.escuchar_con_intentos()
            if respuesta:
                if es_fecha:
                    try:
                        return datetime.strptime(input("Ingresa la fecha y hora (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                    except ValueError:
                        asistente_voz.hablar("Formato de fecha incorrecto. Intenta de nuevo.")
                        continue
                return respuesta
            else:
                asistente_voz.hablar("No te escuché bien. Intenta de nuevo.")

    def crear_clase(self):
        nombre_clase = self.obtener_input_con_reintento("¿Cuál es el nombre de la clase?")
        curso = self.obtener_input_con_reintento("¿Cuál es el curso?")
        fecha = self.obtener_input_con_reintento("¿Cuál es la fecha y hora de la clase? (Formato:YYYY-MM-DD HH:MM)", es_fecha=True)
        if fecha:
            clase = asistente_organizador.crear_clase(nombre_clase, curso, fecha)
            asistente_voz.hablar(f"Clase '{clase.nombre}' creada con éxito.")
           

    def crear_leccion(self):
        while True:
            nombre_clase = self.obtener_input_con_reintento("¿A qué clase deseas agregar una lección?")
            clases = asistente_organizador.buscar_clases(nombre_clase)
            if clases:
                clase = clases[0]
                nombre_leccion = self.obtener_input_con_reintento("¿Cuál es el nombre de la temática?")
                notas = self.obtener_input_con_reintento("¿Cuáles son las notas de la temática?")
                fecha = self.obtener_input_con_reintento("¿Cuál es la fecha de la temática? (Formato:YYYY-MM-DD HH:MM)", es_fecha=True)
                if fecha:
                    leccion = asistente_organizador.agregar_leccion_a_clase(clase, nombre_leccion, notas, fecha)
                    asistente_voz.hablar(f"Temática '{leccion.nombre}' agregada a la clase '{clase.nombre}' con éxito.")
                    break
                else:
                    asistente_voz.hablar("Error al obtener la fecha de la temática. Intenta de nuevo.")
            else:
                asistente_voz.hablar("Clase no encontrada. Intenta de nuevo.")

    def agregar_tarea(self):
        while True:
            nombre_leccion = self.obtener_input_con_reintento("¿A qué temática deseas agregar una tarea?")
            lecciones_encontradas = []
            for clase in asistente_organizador.clases:
                for leccion in clase.lecciones:
                    if nombre_leccion.lower() in leccion.nombre.lower():
                        lecciones_encontradas.append(leccion)

            if lecciones_encontradas:
                if len(lecciones_encontradas) > 1:
                    asistente_voz.hablar("Se encontraron varias temáticas con ese nombre. Por favor, sé más específico.")
                    # Aquí podrías implementar una forma de seleccionar la lección correcta
                else:
                    leccion = lecciones_encontradas[0]
                    descripcion = self.obtener_input_con_reintento("¿Descripción de la tarea?")
                    fecha_entrega = self.obtener_input_con_reintento("¿Fecha de entrega de la tarea? (Formato:YYYY-MM-DD HH:MM)", es_fecha=True)
                    if fecha_entrega:
                        prioridad = self.obtener_input_con_reintento("¿Prioridad de la tarea? (Alta, Media, Baja)").capitalize()
                        tarea = asistente_organizador.agregar_tarea_a_leccion(leccion, descripcion, fecha_entrega, prioridad)
                        asistente_voz.hablar(f"Tarea '{tarea.descripcion}' agregada con éxito.")
                        break
                    else:
                        asistente_voz.hablar("Error al obtener la fecha de entrega. Intenta de nuevo.")
            else:
                asistente_voz.hablar("Temática no encontrada. Intenta de nuevo.")

    def agregar_recordatorio_general(self):
        while True:
            mensaje = self.obtener_input_con_reintento("¿Qué quieres recordar?")
            fecha_str = self.obtener_input_con_reintento("¿Para cuándo quieres el recordatorio? (Formato:YYYY-MM-DD HH:MM, déjalo en blanco para ahora)")
            fecha_hora = None
            if fecha_str:
                try:
                    fecha_hora = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    asistente_voz.hablar("Formato de fecha incorrecto. Intenta de nuevo.")
                    continue
            prioridad = self.obtener_input_con_reintento("¿Cuál es la prioridad? (Alta, Media, Baja)").capitalize()
            asistente_organizador.crear_recordatorio_general(mensaje, fecha_hora, prioridad)
            asistente_voz.hablar("Recordatorio general creado con éxito.")
            self.desbloquear_menu()
            break

    def mostrar_recordatorios(self):
        asistente_voz.hablar("Mostrando todos los recordatorios:")
        asistente_organizador.mostrar_recordatorios()

    def mostrar_clases_y_lecciones(self):
        asistente_voz.hablar("Mostrando clases y lecciones:")
        asistente_organizador.mostrar_clases_y_lecciones()
    
    def desbloquear_menu(self):
        self.menu_desbloqueado = True
        asistente_voz.hablar("Menú completo desbloqueado. Escribe 'menu' para verlo.")

    def ejecutar(self):
        self.mostrar_opciones_iniciales()
        while True:
            asistente_voz.hablar("Dime una opción:")
            opcion = asistente_voz.escuchar_con_intentos().strip().lower()

            if not self.menu_desbloqueado:
                if opcion in ["crear clase", "uno", "1"]:
                    self.crear_clase()
                elif opcion in ["agregar recordatorio general", "dos", "2"]:
                    self.agregar_recordatorio_general()
                elif opcion in ["salir", "tres", "3"]:
                    asistente_organizador.guardar_datos()
                    asistente_voz.hablar(f"Hasta pronto {self.usuario}")
                    break
                elif opcion == "menu":
                    asistente_voz.hablar("Aún no se ha desbloqueado el menú completo. Crea una clase primero.")
                else:
                    asistente_voz.hablar("Opción no válida en el menú inicial. Intenta crear una clase o un recordatorio general. Escribe 'menu' para ver las opciones.")
            else:
                if opcion == "menu":
                    self.mostrar_opciones_completas()
                elif opcion in ["crear clase", "uno", "1"]:
                    self.crear_clase()
                elif opcion in ["crear lección", "dos", "2"]:
                    self.crear_leccion()
                elif opcion in ["agregar tarea", "tres", "3"]:
                    self.agregar_tarea()
                elif opcion in ["agregar recordatorio general", "cuatro", "4"]:
                    self.agregar_recordatorio_general()
                elif opcion in ["mostrar recordatorios", "cinco", "5"]:
                    self.mostrar_recordatorios()
                elif opcion in ["mostrar clases y lecciones", "seis", "6"]:
                    self.mostrar_clases_y_lecciones()
                elif opcion in ["guardar datos", "siete"]:
                    asistente_organizador.guardar_datos()
                    asistente_voz.hablar("Datos guardados.")
                elif opcion in ["salir", "ocho"]:
                    asistente_organizador.guardar_datos()
                    asistente_voz.hablar(f"Hasta pronto {self.usuario}")
                    break
                else:
                    asistente_voz.hablar("Opción no válida, escribe 'menu' para ver las opciones.")



