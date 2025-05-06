import speech_recognition as sr
import pyttsx3

class AsistenteDeVoz:
    def __init__(self, nombre="Asistente"):
        self.nombre = nombre
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

    def escuchar(self):
        while True:
            print("Esperando tu voz... (habla claro)")
            with self.mic as source:
                self.recognizer.adjust_for_ambient_noise(source)
                try:
                    audio = self.recognizer.listen(source, timeout=5)
                    print("Procesando voz...")
                    comando = self.recognizer.recognize_google(audio, language="es-MX")
                    print(f"Escuchado (Google): {comando.lower()}")
                    return comando.lower()
                except sr.WaitTimeoutError:
                    print("No se detectó voz en el tiempo especificado. Intenta de nuevo.")
                    continue
                except sr.UnknownValueError:
                    print("Google Speech Recognition no entendió lo que dijiste. Intenta de nuevo.")
                    continue
                except sr.RequestError as e:
                    print(f"Error con el servicio de Google Speech Recognition: {e}. Intenta de nuevo.")
                    continue

    def escuchar_con_intentos(self, max_intentos=3):
        for i in range(max_intentos):
            texto = self.escuchar() or ""

            if texto.strip():
                return texto

            self.hablar("No te he entendido. Por favor, intenta de nuevo.")

        self.hablar("Por favor escribe tu respuesta:")
        return input().strip()

    def hablar(self, texto):
        print(f"{self.nombre}:", texto)
        self.engine.say(texto)
        self.engine.runAndWait()

if __name__ == "__main__":
    asistente = AsistenteDeVoz("Jarvis")
    asistente.hablar("Hola, ¿en qué puedo ayudarte?")
    comando = asistente.escuchar_con_intentos()
    if comando:
        asistente.hablar(f"Has dicho: {comando}")