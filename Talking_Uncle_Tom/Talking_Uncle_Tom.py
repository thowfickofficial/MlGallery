import pygame
import speech_recognition as sr
import pyttsx3
import os

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("😅Talking Uncle Tom😅")

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the cat image
cat_image_path = os.path.join(script_dir, "cat.jpg")

# Load cat image
cat_image = pygame.image.load(cat_image_path)

# Define the desired size of the image
image_size = (800, 600)  # Adjust the size as needed

# Scale the cat image to the desired size
cat_image = pygame.transform.scale(cat_image, image_size)

# Calculate the position to center the image
cat_x = (WIDTH - image_size[0]) // 2
cat_y = (HEIGHT - image_size[1]) // 2

# Initialize an empty text variable
text = ""

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capture user's speech
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        # Recognize the speech
        user_input = recognizer.recognize_google(audio)
        print(f"You said: {user_input}")

        # Assign the recognized text to the 'text' variable
        text = user_input

        # Speak the user's input
        engine.say(user_input)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    # Clear the screen
    screen.fill((0, 0, 0))

    # Display the cat image and user's input text
    screen.blit(cat_image, (cat_x, cat_y))

    # Render the text on the screen
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

# Quit the game
pygame.quit()
