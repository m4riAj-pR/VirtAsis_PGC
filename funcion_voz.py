import speech_recognition as sr
recognizer = sr.Recognizer()
mic= sr.Microphone()

def escuchar():
    with mic as source:
        print ("Esperando tu voz... (habla claro)")
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="es-CO")        
        print(f"Escuchando..")
        for _ in range (3):
             comando = escuchar_comando()
        if comando:
             break
        print("Intenta de nuevo...")
        return (f"{comando.lower()}")

    except sr.UnknownValueError:
        print("No entendí lo que dijiste...")
        return ""
    except sr.RequestError:
        print ("Servidor inestable")
        return ""



