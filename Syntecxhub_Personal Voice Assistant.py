import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit
import wikipedia

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command

        except sr.UnknownValueError:
            speak("Sorry I did not understand")
            return None

        except sr.RequestError:
            speak("Network error")
            return None


def execute_command(command):

    if command is None:
        return

    try:

        # Tell time
        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        # Open Google
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        # Open YouTube
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        # Play music on YouTube
        elif "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        # Search Wikipedia
        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "")
            speak("Searching Wikipedia")
            result = wikipedia.summary(topic, sentences=2)
            speak(result)

        # Google Search
        elif "search" in command:
            query = command.replace("search", "")
            speak(f"Searching {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        # Exit assistant
        elif "stop" in command or "exit" in command:
            speak("Goodbye")
            exit()

        else:
            speak("Command not recognized")

    except Exception as e:
        print(e)
        speak("Something went wrong")


def main():
    speak("Voice assistant started")

    while True:
        command = listen()
        execute_command(command)


if __name__ == "__main__":
    main()
