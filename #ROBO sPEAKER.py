#ROBO sPEAKER
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Prompt user for input
while True:
    text = input("Enter the text you want to be read aloud: ")

    # Use the engine to say the text
    engine.say(text)

    # Wait for the speech to complete
    engine.runAndWait()