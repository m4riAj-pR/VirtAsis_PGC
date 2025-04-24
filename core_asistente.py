from datetime import datetime, timedelta

class ItemBase:
    def __init__(self, nombre="", notas=""):
        self.nombre = nombre
        self.notas = notas

    def editar(self, nuevo_nombre=None, nuevas_notas=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevas_notas:
            self.notas = nuevas_notas

    def __str__(self):
        return f"{self.nombre} - {self.notas}"

class Clase(ItemBase):
    def __init__(self, nombre, curso, fecha=None):
        super().__init__(nombre,curso)
        self.fecha = fecha or datetime.now()
        self.lecciones = []

    def agregar_leccion(self, nombre, curso, notas, fecha=None):
        leccion = Leccion(nombre, curso, notas, fecha)
        self.lecciones.append(leccion)
        return leccion

    def eliminar_leccion(self, leccion):
        self.lecciones = [l for l in self.lecciones if l != leccion]

    def __str__(self):
        return f"Clase: {self.nombre} | Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')} | Curso: {self.curso}| "

class Leccion(ItemBase):
    def __init__(self, nombre, notas, fecha=None):
        super().__init__(nombre, notas)
        self.fecha = fecha or datetime.now()
        self.tareas = []

    def agregar_tarea(self, descripcion, fecha_entrega, prioridad="Normal"):
        tarea = Tarea(descripcion, fecha_entrega, prioridad)
        self.tareas.append(tarea)
        return tarea

    def __str__(self):
        return f"Lección: {self.nombre} | Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')} | Notas: {self.notas}"

class Tarea:
    def __init__(self, descripcion, fecha_entrega, prioridad="Normal"):
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.prioridad = prioridad

    def crear_recordatorio(self):
        recordatorio_fecha = self.fecha_entrega - timedelta(days=1)  # Recordatorio 1 día antes
        recordatorio = Recordatorio(f"Recordatorio: {self.descripcion}", recordatorio_fecha, self.prioridad)
        return recordatorio

    def __str__(self):
        return f"Tarea: {self.descripcion} | Fecha de entrega: {self.fecha_entrega.strftime('%d/%m/%Y')}"

class Recordatorio:
    def __init__(self, mensaje, fecha_hora=None, prioridad="Normal"):
        self.mensaje = mensaje
        self.fecha = fecha_hora if fecha_hora else datetime.now()
        self.prioridad = prioridad

    def __str__(self):
        return f"Recordatorio: {self.mensaje} | Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}"

class AsistenteVirtual:
    def __init__(self):
        self.clases = []

    def crear_clase(self, nombre, curso, fecha=None):
        nueva_clase = Clase(nombre, curso, fecha)
        self.clases.append(nueva_clase)
        return nueva_clase

    def agregar_leccion_a_clase(self, clase, nombre, notas, fecha=None):
        leccion = clase.agregar_leccion(nombre, notas, fecha)
        return leccion

    def agregar_tarea_a_leccion(self, leccion, descripcion, fecha_entrega, prioridad="Normal"):
        tarea = leccion.agregar_tarea(descripcion, fecha_entrega, prioridad)
        return tarea

    def generar_recordatorios(self):
        recordatorios = []
        for clase in self.clases:
            for leccion in clase.lecciones:
                for tarea in leccion.tareas:
                    recordatorio = tarea.crear_recordatorio()
                    recordatorios.append(recordatorio)
        return recordatorios

    def mostrar_clases_y_lecciones(self):
        for clase in self.clases:
            print(clase)
            for leccion in clase.lecciones:
                print(f"  - {leccion}")
                for tarea in leccion.tareas:
                    print(f"    - {tarea}")
                    print(f"      {tarea.crear_recordatorio()}")

    def mostrar_recordatorios(self):
        recordatorios = self.generar_recordatorios()
        for recordatorio in recordatorios:
            print(recordatorio)

    def buscar_clases(self, nombre_clase):
        coincidencias = []
        for clase in self.clases:
            if nombre_clase.lower() in clase.nombre.lower():
                coincidencias.append(clase)
        return coincidencias
            


