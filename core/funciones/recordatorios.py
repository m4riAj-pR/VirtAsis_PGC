from datetime import datetime

class Recordatorio:
    def __init__(self, mensaje, fecha_hora=None, prioridad="Normal", tipo="general"):
        self.mensaje = mensaje
        self.fecha = fecha_hora if fecha_hora else datetime.now()
        self.prioridad = prioridad
        self.tipo = tipo

    def __str__(self):
        tipo_str = f"({self.tipo.capitalize()})"
        return f"Recordatorio {tipo_str}: {self.mensaje} | Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}"
