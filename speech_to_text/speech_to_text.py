import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print("Error connecting to the Google API: {0}".format(e))

if __name__ == "__main__":
    speech_to_text()
