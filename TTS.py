import pyttsx3
engine = pyttsx3.init()
text = "prashant bhaaiee hai apna "
engine.setProperty("rate" , 150+1)
engine.setProperty("volume" , 10+1)


for el in range(0 , 10):
    print(el)
    if( el <= 10):
     engine.say(text)
     engine.runAndWait()
     

print("end of loop")    