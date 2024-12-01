import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
from openai import OpenAI
from gtts import gTTS
import subprocess
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "<YOUR API KEY>"#NEWSAPI

def speak(text):
    engine.say(text)
    engine.runAndWait()

    
                                  #ignore the commented part 
# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')

# pygame.mixer.init()

# # Load the MP3 file
# pygame.mixer.music.load('temp.mp3')

# # Play the MP3 file
# pygame.mixer.music.play()

# # Wait for the music to finish (optional)
# while pygame.mixer.music.get_busy():  # Check if music is still playing
#     pygame.time.Clock().tick(10)  # Wait a little bit before checking again


#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")

def aiprocess(command):
   client = OpenAI(api_key=" ",
)

   completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
     {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud.give short response please"},
     {"role": "user", "content": command}
  ] 
)

   return completion.choices[0].message.content


def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://www.google.com/")
   elif "open youtube" in c.lower():
      webbrowser.open("https://www.youtube.com/")
   elif "open github" in c.lower():
      webbrowser.open("https://github.com/")
   elif "open snapchat" in c.lower():
      webbrowser.open("https://www.snapchat.com/")
   elif "open instagram" in c.lower():
      webbrowser.open("https://www.instagram.com/")
   elif "open whatsapp" in c.lower():
      webbrowser.open("https://web.whatsapp.com/")
   

   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = music_library.music[song]
      webbrowser.open(link)
  

   elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
   else:
      #let open ai handle the request
      output = aiprocess(c)
      speak(output)
      pass
      


if __name__ == "__main__":
  speak("Initializing jarvis......")

  while True:
  #listen for wake word jarvis
  # obtain audio from the microphone
    r = sr.Recognizer()
   

    print("recognizing")
# recognize speech using Sphinx
    try:
         with sr.Microphone() as source:
            print("Listening..") 
            audio = r.listen(source, timeout=2,phrase_time_limit= 1)
         word = command = r.recognize_google(audio)
         if(word.lower()=="jarvis"):
            speak("i am here")
            #listen command 
            with sr.Microphone() as source:
             print("jarvis active..") 
             audio = r.listen(source) 
             command = r.recognize_google(audio)

             processCommand(command)

    except  Exception as e:
        print("Error; {0}".format(e))