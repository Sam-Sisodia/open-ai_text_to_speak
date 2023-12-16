# import speech_recognition as sr

# def speech_to_text():
#     # Initialize the recognizer
#     recognizer = sr.Recognizer()

#     # Capture audio from the microphone
#     with sr.Microphone() as source:
#         print("Say something:")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#         audio = recognizer.listen(source, timeout=5)

#     try:
#         # Recognize speech using Google Speech Recognition
#         text = recognizer.recognize_google(audio)
#         print("You said: {}".format(text))
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# if __name__ == "__main__":
#     speech_to_text()
