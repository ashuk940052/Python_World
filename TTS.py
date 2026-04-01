import pyttsx3
engine = pyttsx3.init()
text = " This is my first programme for Text to speech "
engine.setProperty('rate' , 150)
engine.setProperty('vilome' , 10)
engine.say(text)
engine.runAndWait()