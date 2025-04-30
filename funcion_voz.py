import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
mic= sr.Microphone()
engine = pyttsx3.init()
engine.setProperty('rate', 150)


def escuchar():
    while True:
        print("Esperando tu voz... (habla claro)")
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)
                print("Procesando voz...")
                comando = recognizer.recognize_google(audio, language="es-MX")
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
    

def escuchar_con_intentos(max_intentos=3):
    for i in range(max_intentos):
        texto = escuchar() or ""
        
        if texto.strip():  
            return texto
        
        hablar("No te he entendido. Por favor, intenta de nuevo.")
    
    hablar("Por favor escribe tu respuesta:")
    return input().strip()  

def hablar(texto):
    print("Asistente:", texto)
    engine.say(texto)
    engine.runAndWait()