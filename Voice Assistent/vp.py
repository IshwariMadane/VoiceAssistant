import speech_recognition as sr
import pyttsx3
import webbrowser

def play_video(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)

def assistant():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("User Query:", query)
            if 'exit' in query:
                print("Exiting...")
                break
            else:
                print("Playing video for query:", query)
                engine.say(f"Playing video for query {query}")
                engine.runAndWait()
                play_video(query)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Sorry, I couldn't request results. Please check your internet connection.")

if __name__ == "__main__":
    assistant()