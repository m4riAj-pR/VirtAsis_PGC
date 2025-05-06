from datetime import datetime
from core.asistente_virtual import AsistenteVirtual
from core.funciones.clases_docente import ClasesDocente
from core.funciones.recordatorios import Recordatorio
from core.funciones.lecciones import Leccion
from core.funciones.tareas import Tarea
import json

NOMBRE_ARCHIVO = "asistente_data.json"

class AsistenteConPersistencia(AsistenteVirtual):
    def __init__(self):
        super().__init__()
        self.cargar_datos()

    def _formatear_datetime(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    def guardar_datos(self):
        data = {
            "clases": [self._clase_a_dict(clase) for clase in self.clases],
            "recordatorios_generales": [self._recordatorio_a_dict(rec) for rec in self.recordatorios_generales],
        }
        with open(NOMBRE_ARCHIVO, 'w') as f:
            json.dump(data, f, default=self._formatear_datetime, indent=4)
        print(f"Datos guardados en {NOMBRE_ARCHIVO}")

    def cargar_datos(self):
        try:
            with open(NOMBRE_ARCHIVO, 'r') as f:
                data = json.load(f)
                self.clases = [self._clase_desde_dict(clase_data) for clase_data in data.get("clases", [])]
                self.recordatorios_generales = [self._recordatorio_desde_dict(rec_data) for rec_data in data.get("recordatorios_generales", [])]
            print(f"Datos cargados desde {NOMBRE_ARCHIVO}")
        except FileNotFoundError:
            print(f"Archivo {NOMBRE_ARCHIVO} no encontrado. Se iniciará con datos vacíos.")
        except json.JSONDecodeError:
            print(f"Error al decodificar {NOMBRE_ARCHIVO}. Se iniciará con datos vacíos.")

    def _item_base_a_dict(self, item):
        return {"nombre": item.nombre, "notas": item.notas}

    def _item_base_desde_dict(self, data, item_class):
        return item_class(nombre=data.get("nombre", ""), notas=data.get("notas", ""))

    def _clase_a_dict(self, clase):
        data = self._item_base_a_dict(clase)
        data["curso"] = clase.curso
        data["fecha"] = clase.fecha
        data["lecciones"] = [self._leccion_a_dict(leccion) for leccion in clase.lecciones]
        data["recordatorios_clase"] = [self._recordatorio_a_dict(rec) for rec in clase.recordatorios_clase]
        return data
    
    def _clase_desde_dict(self, data):
        clase = ClasesDocente(nombre=data.get("nombre", ""), curso=data.get("curso", ""), fecha=datetime.fromisoformat(data.get("fecha")) if data.get("fecha") else None)
        clase.lecciones = [self._leccion_desde_dict(leccion_data) for leccion_data in data.get("lecciones", [])]
        clase.recordatorios_clase = [self._recordatorio_desde_dict(rec_data) for rec_data in data.get("recordatorios_clase", [])]
        return clase

    def _leccion_a_dict(self, leccion):
        data = self._item_base_a_dict(leccion)
        data["fecha"] = leccion.fecha
        data["tareas"] = [self._tarea_a_dict(tarea) for tarea in leccion.tareas]
        return data

    def _leccion_desde_dict(self, data):
        leccion = Leccion(nombre=data.get("nombre", ""), notas=data.get("notas", ""), fecha=datetime.fromisoformat(data.get("fecha")) if data.get("fecha") else None)
        leccion.tareas = [self._tarea_desde_dict(tarea_data) for tarea_data in data.get("tareas", [])]
        return leccion

    def _tarea_a_dict(self, tarea):
        return {
            "descripcion": tarea.descripcion,
            "fecha_entrega": tarea.fecha_entrega,
            "prioridad": tarea.prioridad,
        }

    def _tarea_desde_dict(self, data):
        return Tarea(descripcion=data.get("descripcion", ""), fecha_entrega=datetime.fromisoformat(data.get("fecha_entrega")) if data.get("fecha_entrega") else None, prioridad=data.get("prioridad", "Normal"))

    def _recordatorio_a_dict(self, recordatorio):
        return {
            "mensaje": recordatorio.mensaje,
            "fecha": recordatorio.fecha,
            "prioridad": recordatorio.prioridad,
            "tipo": recordatorio.tipo,
        }

    def _recordatorio_desde_dict(self, data):
        return Recordatorio(mensaje=data.get("mensaje", ""), fecha_hora=datetime.fromisoformat(data.get("fecha")) if data.get("fecha") else None, prioridad=data.get("prioridad", "Normal"), tipo=data.get("tipo", "general"))
