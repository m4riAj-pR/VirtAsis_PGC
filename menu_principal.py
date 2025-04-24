from core_asistente import AsistenteVirtual
from funcion_voz import *
from datetime import datetime


asistente = AsistenteVirtual()

class Menu:
    def __init__(self, usuario):
        self.usuario = usuario


    def mostrar_opciones(self):
        hablar(f"Hola {self.usuario}, soy Zeta, tu asistente virtual.")
        hablar("Estas son las opciones disponibles:")
        hablar("""
1. Crear clase
2. Crear lección dentro de una clase
3. Agregar tarea a lección
4. Agregar recordatorio automático
5. Editar tarea
6. Eliminar tarea
7. Buscar clases
8. Buscar lecciones
9. Mostrar clases y lecciones
10. Salir
""")

    def ejecutar(self):
        while True:
            hablar("Dime una opción:")
            opcion = escuchar_con_intentos().lower()

            if "crear clase" in opcion:
                self.crear_clase()
            elif "crear lección" in opcion:
                self.crear_leccion()
            elif "agregar tarea" in opcion:
                self.agregar_tarea()
            elif "agregar recordatorio" in opcion:
                self.agregar_recordatorio()
            elif "editar tarea" in opcion:
                self.editar_tarea()
            elif "eliminar tarea" in opcion:
                self.eliminar_tarea()
            elif "buscar clases" in opcion:
                self.buscar_clase()
            elif "buscar lecciones" in opcion:
                self.buscar_leccion()
            elif "mostrar clases y lecciones" in opcion:
                self.mostrar_clases_y_lecciones()
            elif "salir" in opcion:
                hablar(f"Hasta pronto {self.usuario.obtener_primer_nombre()}.")
                break
            else:
                hablar("Opción no válida, intenta de nuevo.")

    def crear_clase(self):
        hablar("¿Cuál es el nombre de la clase?")
        nombre_clase = escuchar_con_intentos()
        hablar("¿Cual es el curso?")
        curso = input()
        hablar("¿Cuál es la fecha y hora de la clase? (Formato: YYYY-MM-DD HH:MM)")
        fecha_input = input()
        fecha = datetime.strptime(fecha_input, "%Y-%m-%d %H:%M")
        clase = asistente.crear_clase(nombre_clase, curso, fecha)
        hablar(f"Clase '{clase.nombre}' creada con éxito.")

    def crear_leccion(self):
        hablar("¿A qué clase deseas agregar una lección?")
        nombre_clase = escuchar()
        clases = asistente.buscar_clases(nombre_clase)
        if clases:
            clase = clases[0]
            hablar("¿Cuál es el nombre de la tematica?")
            nombre_leccion = escuchar_con_intentos()
            hablar("¿Cuáles son las notas de la tematica?")
            notas = escuchar_con_intentos()
            hablar("¿Cuál es la fecha de la tematica? (Formato: YYYY-MM-DD HH:MM)")
            fecha_input = input()
            fecha = datetime.strptime(fecha_input, "%Y-%m-%d %H:%M")
            leccion = clase.agregar_leccion(nombre_leccion, notas, fecha)
            hablar(f"tematica'{leccion.nombre}' agregada a la clase '{clase.nombre}' con éxito.")
        else:
            hablar("Clase no encontrada. Primero crea una clase.")

    def agregar_tarea(self):
        hablar("¿A qué tematica deseas agregar una tarea?")
        nombre_leccion = escuchar_con_intentos()
        lecciones = asistente.buscar_lecciones(nombre_leccion)
        if lecciones:
            hablar("¿Descripción de la tarea?")
            descripcion = escuchar_con_intentos()
            hablar("¿Fecha de entrega de la tarea? (Formato: YYYY-MM-DD HH:MM)")
            fecha_input = input()
            fecha = datetime.strptime(fecha_input, "%Y-%m-%d %H:%M")
            hablar("¿Prioridad de la tarea?, (Alta, Media, Baja)")
            prioridad = escuchar_con_intentos()
            tarea = lecciones[0].agregar_tarea(descripcion, fecha, prioridad)
            hablar(f"Tarea '{tarea.descripcion}' agregada con éxito.")
        else:
            hablar("tematica no encontrada. Primero crea una tematica.")

    def agregar_recordatorio(self):
        hablar("¿Para qué tarea deseas agregar un recordatorio?")
        nombre_tarea = escuchar()
        tarea = asistente.buscar_tareas(nombre_tarea)
        if tarea:
            recordatorio = tarea[0].crear_recordatorio()  
            hablar(f"Recordatorio agregado: {recordatorio}")
        else:
            hablar("Tarea no encontrada. Primero agrega una tarea.")

    def editar_tarea(self):
        hablar("¿Cuál es el nombre de la tarea que deseas editar?")
        nombre_tarea = escuchar()
        tarea = asistente.buscar_tareas(nombre_tarea)
        if tarea:
            hablar("Nuevo nombre de la tarea:")
            nuevo_nombre = escuchar()
            hablar("Nueva descripción:")
            nueva_desc = escuchar()
            hablar("Nueva fecha de entrega (Formato: YYYY-MM-DD HH:MM):")
            nueva_fecha = input()
            tarea[0].descripcion = nuevo_nombre
            tarea[0].fecha_entrega = datetime.strptime(nueva_fecha, "%Y-%m-%d %H:%M")
            hablar("Tarea actualizada.")
        else:
            hablar("Tarea no encontrada.")

    def eliminar_tarea(self):
        hablar("¿Cuál es el nombre de la tarea que deseas eliminar?")
        nombre_tarea = escuchar()
        tarea = asistente.buscar_tareas(nombre_tarea)
        if tarea:
            leccion = asistente.buscar_lecciones(tarea[0].descripcion)
            leccion[0].eliminar_tarea(tarea[0])
            hablar(f"Tarea '{nombre_tarea}' eliminada con éxito.")
        else:
            hablar("Tarea no encontrada.")

    def buscar_clase(self):
        hablar("¿Qué clase deseas buscar?")
        nombre_clase = escuchar()
        clases = asistente.buscar_clases(nombre_clase)
        if clases:
            for clase in clases:
                hablar(f"- {clase}")
        else:
            hablar("Clase no encontrada.")

    def buscar_leccion(self):
        hablar("¿Qué tematica deseas buscar?")
        nombre_leccion = escuchar()
        lecciones = asistente.buscar_lecciones(nombre_leccion)
        if lecciones:
            for leccion in lecciones:
                hablar(f"- {leccion}")
        else:
            hablar("Lección no encontrada.")

    def mostrar_clases_y_lecciones(self):
        hablar("Mostrando todas las clases y lecciones:")
        asistente.mostrar_clases_y_lecciones()

    def mostrar_menu(self):
        self.mostrar_opciones()
        self.ejecutar()


     # ← lanza el menú por voz
