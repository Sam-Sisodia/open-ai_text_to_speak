import pyttsx3
import time
# initialize Text-to-speech engine.
engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume',1.0)
voices = engine.getProperty("voices")
text = "What is python"
engine.say(text)



# for i in voices:
#     engine.setProperty("voice",i.id)
# # convert this text to speech.
#     text = "Sajal is good boy"
#     engine.say(text)
#     engine.runAndWait()
#     # time.sleep(1)
#     print("This is ----",i.id)

# # play the speech.

engine.stop()