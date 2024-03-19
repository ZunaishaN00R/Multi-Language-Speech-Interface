#  only writing
import speech_recognition as sr
import pyttsx3

def speak(Text):
    engine = pyttsx3.init("sapi5")
    voice = engine.getProperty("voices")
    engine.setProperty("voice", voice[0].id)
    engine.setProperty("rate", 200)
    print(f"My Model : {Text}")
    engine.say(text=Text)
    engine.runAndWait()

def listen_and_speak():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        audio = r.listen(source, phrase_time_limit=5)

        try:
            query = r.recognize_google(audio, language="ur-PK")  # Recognize Arabic
            print(f"You (Arabic): {query}")
            speak(query)
        except Exception:
            try:
                query = r.recognize_google(audio, language="ar-SA")  # Recognize Urdu
                print(f"You (Urdu): {query}")
                speak(query)
            except Exception:
                try:
                    query = r.recognize_google(audio, language="en-PK")  # Recognize English in Pakistan dialect
                    print(f"You (English): {query}")
                    speak(query)
                except Exception as e:
                    print(e)
                    speak("Sorry, I couldn't understand your request.")

if __name__ == '__main__':
    while True:
        listen_and_speak()