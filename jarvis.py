

from openai import OpenAI
import os

import pyttsx3
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
from playsound import playsound
# initialize Text-to-speech engine.
engine = pyttsx3.init()



client =OpenAI(api_key="")

client = client
prompt = "Sajal Sisodia the python developer?"


response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    temperature=0,
    messages=[
        {
            "role": "user",
            "content" : f" write 50 words on the give {prompt}" 
        }
    ]
)

response = response.choices[0].message.content.strip()
print(response+ "Thank you")

# engine.say(response)


language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=response + "Thank you", lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("temp.mp3")
playsound("temp.mp3")
os.remove("temp.mp3")

# play the speech.
engine.runAndWait()
