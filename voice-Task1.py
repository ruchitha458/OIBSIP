import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def get_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you repeat?")
        return get_command()
    except sr.RequestError:
        speak("Sorry, I couldn't access the Google Speech Recognition service.")
        return ""

def main():
    greet()
    speak("How can I assist you?")
    while True:
        command = get_command()
        if any(greeting in command for greeting in ["hi", "hello"]):
            speak("Hello! How can I assist you?")
        elif "how are you" in command:
            speak("I'm doing well, thank you for asking!")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {current_date}")
        elif "search" in command:
            speak("What do you want to search for?")
            search_query = get_command()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                speak(f"Here are the search results for {search_query}")
        elif "exit" in command or "bye" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
