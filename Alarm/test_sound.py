import pygame
import os
import time

# Initialize pygame mixer
pygame.mixer.init()

def play_test_sound(sound_file):
    if os.path.isfile(sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        print("Playing sound...")
        time.sleep(5)  # Play for 5 seconds
        pygame.mixer.music.stop()
    else:
        print(f"Sound file {sound_file} does not exist.")

if __name__ == "__main__":
    # Path to your sound file
    sound_file = os.path.expanduser("~/Hudba/Budík/Wilhelm scream Sound.wav")
    play_test_sound(sound_file)

