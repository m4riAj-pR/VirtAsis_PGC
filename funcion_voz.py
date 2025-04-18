import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

def escuchar():
    for intento in range(3):
        with mic as source:
            print("Di algo... (habla claro)")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)  # Escucha hasta que haya silencio

        try:
            texto = recognizer.recognize_google(audio, language="es-CO")
            print(f"Entendí: {texto}")
            return texto.lower()  # Devuelve el texto en minúsculas
        except sr.UnknownValueError:
            print("No entendí, repite por favor.")
            return ""
        except sr.RequestError:
            print("Error de conexión con Google.")
            return ""
    return ""
    

# Ejemplo de uso:
comando = escuchar()
if comando:
    print("Comando recibido:", comando)
else:
    print("No se detectó voz válida.")