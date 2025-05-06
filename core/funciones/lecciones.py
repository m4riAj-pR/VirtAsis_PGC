from core.funciones.base import ItemBase
from datetime import datetime
from core.funciones.tareas import Tarea

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
