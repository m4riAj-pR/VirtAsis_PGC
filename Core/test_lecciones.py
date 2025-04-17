from core_asistente import Asistente_virtual
from datetime import datetime

# Creamos el asistente
asistente = Asistente_virtual()

def menu():
    print("\n--- Asistente del Docente ---")
    print("1. Crear nueva lección")
    print("2. Agregar temática a una lección")
    print("3. Agregar recordatorio")
    print("4. Ver lecciones y contenido")
    print("5. Buscar lecciones")
    print("6. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la lección: ")
        horario = input("Horario (ej. Lunes 10:00 AM): ")
        asistente.crear_leccion(nombre, horario)
        print("✅ Lección creada.")

    elif opcion == "2":
        for i, lec in enumerate(asistente.lecciones):
            print(f"{i + 1}. {lec}")
        idx = int(input("Selecciona una lección: ")) - 1
        nombre_tema = input("Nombre de la temática: ")
        descripcion = input("Descripción breve: ")
        asistente.lecciones[idx].agg_tematica(nombre_tema, descripcion)
        print("✅ Temática agregada.")

    elif opcion == "3":
        for i, lec in enumerate(asistente.lecciones):
            print(f"{i + 1}. {lec}")
        idx = int(input("Selecciona una lección: ")) - 1
        mensaje = input("Mensaje del recordatorio: ")
        fecha_input = input("Fecha y hora (dd/mm/yyyy hh:mm): ")
        fecha = datetime.strptime(fecha_input, "%d/%m/%Y %H:%M")
        asistente.lecciones[idx].agg_recordatorio(mensaje, fecha)
        print("✅ Recordatorio agregado.")

    elif opcion == "4":
        for leccion in asistente.lecciones:
            print(f"\n📚 {leccion}")
            print("Temáticas:")
            for tema in leccion.tematicas:
                print("  -", tema)
            print("Recordatorios:")
            for rec in leccion.recordatorios:
                print("  -", rec)

    elif opcion == "5":
        consulta = input("Buscar por nombre de lección: ")
        resultado = asistente.buscar_lecciones(consulta)
        if isinstance(resultado, str):
            print("❌", resultado)
        else:
            for lec in resultado:
                print("🔎", lec)

    elif opcion == "6":
        print("👋 Hasta luego, profe.")
        break

    else:
        print("⚠️ Opción no válida. Intenta otra vez.")
