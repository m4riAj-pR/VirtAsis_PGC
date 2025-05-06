from datetime import timedelta
from core.funciones.recordatorios import Recordatorio

class Tarea:
    def __init__(self, descripcion, fecha_entrega, prioridad="Normal"):
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.prioridad = prioridad

    def crear_recordatorio(self):
        recordatorio_fecha = self.fecha_entrega - timedelta(days=1) 
        recordatorio = Recordatorio(f"Recordatorio: {self.descripcion}", recordatorio_fecha, self.prioridad, tipo="tarea")
        return recordatorio

    def __str__(self):
        return f"Tarea: {self.descripcion} | Fecha de entrega: {self.fecha_entrega.strftime('%d/%m/%Y')}"