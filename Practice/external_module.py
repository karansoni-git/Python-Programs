import pyttsx3

engine = pyttsx3.init()

engine.say("this is an example of python practice programs and this is an external module which convert text to speech and speak the exact text")
engine.runAndWait()
print("text spoke successfully")