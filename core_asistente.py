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

class Clases(ItemBase):
    def __init__(self, nombre, curso, fecha=None):
        super().__init__(nombre,curso)
        self.fecha = fecha or datetime.now()
        self.lecciones = []
        self.recordatorios_clase = [] # Lista para recordatorios automáticos de la clase
        self._generar_recordatorio_automatico()

    def _generar_recordatorio_automatico(self):
        # Generar un recordatorio automático 1 hora antes de la clase
        if self.fecha:
            recordatorio_fecha = self.fecha - timedelta(hours=1)
            mensaje = f"Recordatorio: Clase de {self.nombre} ({self.curso})"
            recordatorio = Recordatorio(mensaje, recordatorio_fecha, prioridad="Normal", tipo="clase")
            self.recordatorios_clase.append(recordatorio)

    def agregar_leccion(self, nombre, curso, notas, fecha=None):
        leccion = Leccion(nombre, curso, notas, fecha)
        self.lecciones.append(leccion)
        return leccion

    def eliminar_leccion(self, leccion):
        self.lecciones = [l for l in self.lecciones if l != leccion]

    def __str__(self):
        recordatorios_str = ", ".join(str(r) for r in self.recordatorios_clase) if self.recordatorios_clase else "Ninguno"
        return f"Clase: {self.nombre} | Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')} | Curso: {self.curso} | Recordatorios: [{recordatorios_str}]"

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
        recordatorio = Recordatorio(f"Recordatorio: {self.descripcion}", recordatorio_fecha, self.prioridad, tipo="tarea")
        return recordatorio

    def __str__(self):
        return f"Tarea: {self.descripcion} | Fecha de entrega: {self.fecha_entrega.strftime('%d/%m/%Y')}"

class Recordatorio:
    def __init__(self, mensaje, fecha_hora=None, prioridad="Normal", tipo="general"):
        self.mensaje = mensaje
        self.fecha = fecha_hora if fecha_hora else datetime.now()
        self.prioridad = prioridad
        self.tipo = tipo # 'clase', 'tarea', 'general'

    def __str__(self):
        tipo_str = f"({self.tipo.capitalize()})"
        return f"Recordatorio {tipo_str}: {self.mensaje} | Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}"

class AsistenteVirtual:
    def __init__(self):
        self.clases = []
        self.recordatorios_generales = [] # Lista para recordatorios creados por el usuario

    def crear_clase(self, nombre, curso, fecha=None):
        nueva_clase = Clases(nombre, curso, fecha)
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
            recordatorios.extend(clase.recordatorios_clase) 
            for leccion in clase.lecciones:
                for tarea in leccion.tareas:
                    recordatorio = tarea.crear_recordatorio()
                    recordatorios.append(recordatorio)
        recordatorios.extend(self.recordatorios_generales) 

    def crear_recordatorio_general(self, mensaje, fecha_hora=None, prioridad="Normal"):
        nuevo_recordatorio = Recordatorio(mensaje, fecha_hora, prioridad, tipo="general")
        self.recordatorios_generales.append(nuevo_recordatorio)
        return nuevo_recordatorio

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


