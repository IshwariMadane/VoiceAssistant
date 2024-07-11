import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
from bs4 import BeautifulSoup

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
#search the query
def get_web_data(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', class_='BNeawe iBp4i AP7Wnd')
    if search_results:
        return search_results[0].get_text()
    else:
        return "Sorry, I couldn't find relevant information."
# playing video
def  play_video(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)
# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")
        return ""


# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak("The current time is " + current_time)


# Function to get the current date
def get_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    speak("Today is " + current_date)


# Main function
if __name__ == "__main__":
    speak("Hey Ishwari! I am your Voice Assistant ")

    while True:
        query = recognize_speech().lower()

        if "hi" in query or "hello" in query or "what's going on" in query:
            speak("My Pleasure ,How can I assist you?")

        elif "how are you" in query:
            speak("I'm fine, thank you!")

        elif "what's the time" in query or "  tell me the time" in query:
            get_time()

        elif "what's the date" in query or "tell me the date" in query:
            get_date()

        elif "search" in query  or "what "in query or "how" in query:
            speak("ok searching")

            search_query = recognize_speech().lower()
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            break
            what_query = recognize_speech().lower()
            what_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(what_url)
            break

            how_query = recognize_speech().lower()
            how_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(how_url)
            break

        elif "play"in query:
            speak("ok")
            play_query = recognize_speech().lower()
            play_query = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(play_query)
            speak("Here are the search results  " )

        elif "exit" in query or "bye" in query:
            speak("Goodbye!")
            break
        else:
            speak("sorry! I couldn't understand" )