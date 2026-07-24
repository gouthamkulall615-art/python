import speech_recognition as sr
import pyttsx3
import time

recognizer = sr.Recognizer()


def speak(text):
    print(f"Jarvis: {text}")
    engine = (
        pyttsx3.init()
    )  # fresh engine each call fixes the "silent after first call" bug
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # release resources cleanly


def processCommand(command):
    print(f"Command: {command}")
    speak(f"You said {command}")


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5)

            word = recognizer.recognize_google(audio)
            print(f"Recognized: {word}")

            if "jarvis" in word.lower():
                print("Wake word detected")
                speak("Yes, I am listening")  # now correctly inside the if-block

                time.sleep(1)

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                processCommand(command)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Speech Recognition service error: {e}")
        except Exception as e:
            print(f"Error: {e}")
