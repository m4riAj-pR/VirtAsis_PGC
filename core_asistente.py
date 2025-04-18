from datetime import datetime

class Tematica:
    def __init__(self, nombre="", descripcion=""):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"

class Recordatorio:
    def __init__(self, fecha_hora, mensaje):
        self.mensaje = mensaje
        self.fecha = fecha_hora

    def __str__(self):
        return f"{self.mensaje} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"

class Leccion:
    def __init__(self, nombre, horario):
        self.nombre = nombre
        self.horario = horario
        self.tematicas = []
        self.recordatorios = []

    def agg_tematica(self, nombre_tema="", descripcion=""):
        self.tematicas.append(Tematica(nombre_tema, descripcion))

    def agg_recordatorio(self, mensaje, fecha=None):
        if fecha is None:
            fecha = datetime.now()
        self.recordatorios.append(Recordatorio(fecha, mensaje))

    def __str__(self):
        return f"{self.nombre} ({self.horario})"

class Asistente_virtual:
    def __init__(self):
        self.lecciones = []

    def crear_leccion(self, nombre, horario):
        nueva_leccion = Leccion(nombre, horario)
        self.lecciones.append(nueva_leccion)

    def buscar_lecciones(self, nombre):
        lecciones_encontradas = []
        for leccion in self.lecciones:
            if nombre.lower() in leccion.nombre.lower():
                lecciones_encontradas.append(leccion)

        if not lecciones_encontradas:
            return "No se encontraron lecciones"

        return lecciones_encontradas
