from core.funciones.base import ItemBase
from core.funciones.recordatorios import Recordatorio
from core.funciones.lecciones import Leccion
from datetime import datetime, timedelta

class ClasesDocente(ItemBase):
    def __init__(self, nombre, curso, fecha=None):
        super().__init__(nombre,curso)
        self.fecha = fecha or datetime.now()
        self.lecciones = []
        self.recordatorios_clase = [] 
        self.curso = []
        self._generar_recordatorio_automatico()

    def _generar_recordatorio_automatico(self):
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