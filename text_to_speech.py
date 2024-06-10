import pyttsx3

def generate_audio(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  

    # Set the voice (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.say(text)
    engine.runAndWait()
