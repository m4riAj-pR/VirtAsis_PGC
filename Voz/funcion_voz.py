import speech_recognition as sr
import pyttsx3
recognizer = sr.Recognizer()
mic= sr.Microphone()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def escuchar():
    with mic as source:
        print ("Esperando tu voz... (habla claro)")
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-CO")        
        print(f"Escuchando..")
        return (f"{comando.lower()}")

    except sr.UnknownValueError:
        print("No entendí lo que dijiste...")
        return ""
    except sr.RequestError:
        print ("Servidor inestable")
        return ""

def escuchar_con_intentos(max_intentos=3):
    for intento in range(max_intentos):
        texto = escuchar()
        if texto and texto.strip():
            return texto
            
        hablar("No te he entendido. Por favor, intenta de nuevo.")
    hablar("Por favor escribe tu respuesta:")
    return input().strip()

def hablar(texto):
    print("Asistente:", texto)
    engine.say(texto)
    engine.runAndWait()







