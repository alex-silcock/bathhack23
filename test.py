import pygame
# Initialize Pygame
pygame.mixer.init()

# Set the number of mixer channels
pygame.mixer.set_num_channels(3)

# Load the sound files
sound1 = pygame.mixer.Sound('high-hat.wav')
sound2 = pygame.mixer.Sound('bass.wav')
sound3 = pygame.mixer.Sound('synth-chord.wav')

# Define a function to play sounds based on input
def play_sound(input):
    if input == 1:
        channel = pygame.mixer.Channel(0)
        channel.play(sound1)
    elif input == 2:
        channel = pygame.mixer.Channel(1)
        channel.play(sound2)
    elif input == 3:
        channel = pygame.mixer.Channel(2)
        channel.play(sound3)

if __name__ == "__main__":
    play_sound(1)