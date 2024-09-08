import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    # Get user input
    x = input("Enter your sentence (type 'exit' to quit): ")

    # Check if the user wants to exit
    if x.lower() == 'exit':
        print("Exiting...")
        break

    # Use the engine to speak the sentence
    engine.say(x)

    # Wait for the speech to finish
    engine.runAndWait()
