import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")



while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        if(command.lower()=="jarvis"):
         speak("ya")

    except sr.WaitTimeoutError:
        print("No one spoke.")
        continue

    except sr.UnknownValueError:
        print("Couldn't understand.")

    except sr.RequestError as e:
        print(e)