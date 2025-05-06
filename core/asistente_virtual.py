from core.funciones.clases_docente import ClasesDocente
from core.funciones.recordatorios import Recordatorio

class AsistenteVirtual:
    def __init__(self):
        self.clases = []
        self.recordatorios_generales = [] 

    def crear_clase(self, nombre, curso, fecha=None):
        nueva_clase = ClasesDocente(nombre, curso, fecha)
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

