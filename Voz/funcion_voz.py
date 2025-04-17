import speech_recognition as sr
recognoizer = sr.Recognizer()
mic= sr.Microphone()
def escuchar():
    with mic as source:
        print("Escuchando...")
        audio = recognoizer.listen(source)
        texto = recognoizer.recognize_google(audio, language="es-ES")
        
        return texto
print (escuchar())

