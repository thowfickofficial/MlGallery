import csv
import random
import spacy
from colorama import Fore, Style, init
from pyfiglet import Figlet

# Initialize colorama for text coloring
init(autoreset=True)

# Create a custom Figlet font for the title
title_font = Figlet(font='slant')

# Load jokes from the CSV file into a list
jokes = []

# Use the absolute path to 'jokes.csv'
with open('/home/tf/thowfick_official/thowfick_official_github/ShortJoke_AI/jokes.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        jokes.append(row['Joke'])

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Function to generate a random joke
def generate_joke():
    return random.choice(jokes)

# Function to handle user input and generate responses
def chatbot(input_text):
    doc = nlp(input_text.lower())
    
    if "joke" in [token.text for token in doc]:
        return generate_joke()
    elif "quit" in [token.text for token in doc]:
        return "Goodbye! Have a great day."
    else:
        return "I didn't understand that. Would you like to hear a joke or quit?"

# Print a colorful title
print(Fore.CYAN + Style.BRIGHT + title_font.renderText("Joke-telling AI"))
print(Style.RESET_ALL)
print("Hello! I'm your joke-telling AI. You can ask for a joke or type 'Quit' to exit.")

# User interaction loop
while True:
    user_input = input("> ")
    response = chatbot(user_input)
    
    # Colorize the response
    if "Goodbye" in response:
        print(Fore.GREEN + Style.BRIGHT + response)
        print(Style.RESET_ALL)
        break
    elif "I didn't understand" in response:
        print(Fore.YELLOW + Style.BRIGHT + response)
        print(Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + Style.BRIGHT + response)
        print(Style.RESET_ALL)
