import os
import time
import threading
import pygame
import sys

stop_event = threading.Event()
continue_event = threading.Event()

def play_sound(sound_file):
    if os.path.isfile(sound_file):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play(-1)  # Play the sound indefinitely

        while not stop_event.is_set():
            time.sleep(0.1)  # Check the stop event periodically

        pygame.mixer.music.stop()
    else:
        print(f"Sound file {sound_file} does not exist.")

def print_progress_bar(elapsed_time, total_time, width=50):
    progress = int(elapsed_time / total_time * width)
    bar = f"|{'=' * progress}{' ' * (width - progress)}|"
    remaining_time = int(total_time - elapsed_time)
    minutes, seconds = divmod(remaining_time, 60)
    print(f"\r{bar} {minutes:02d}:{seconds:02d} remaining", end="")

def countdown_timer(duration, repeat, sound_file=None):
    iteration = 0
    while repeat == -1 or iteration < repeat:
        iteration += 1
        start_time = time.time()
        while time.time() - start_time < duration:
            elapsed_time = time.time() - start_time
            print_progress_bar(elapsed_time, duration)
            time.sleep(0.1)
        print(f"\r|{'=' * 50}| 00:00 remaining", end="")
        print("\nTime's up!")

        if sound_file:
            stop_event.clear()
            continue_event.clear()
            sound_thread = threading.Thread(target=play_sound, args=(sound_file,))
            sound_thread.start()

            print("Press Enter to stop the sound.")
            input()  # Wait for the first Enter
            stop_event.set()

            print("Press Enter to continue to the next cycle.")
            input()  # Wait for the second Enter
            continue_event.set()
            sound_thread.join()  # Ensure the sound thread is properly stopped

if __name__ == "__main__":
    os.system('wcalc')  # Launch the calculator application
    try:
        duration_minutes = float(input("Enter countdown duration in minutes: "))
        repeat_input = input("Enter number of repetitions (or 'i' for infinite): ")
        if repeat_input.lower() == 'i':
            repeat = -1
        else:
            repeat = int(repeat_input)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)

    sound_dir = os.path.expanduser("~/Hudba/Budík")
    sounds = [f for f in os.listdir(sound_dir) if f.endswith('.wav')]

    if not sounds:
        print("No .wav files found in ~/Hudba/Budík.")
        sys.exit(1)

    print("Choose a sound:")
    for idx, sound in enumerate(sounds, 1):
        print(f"{idx}. {sound}")

    try:
        sound_option = int(input("Enter your choice: "))
        if 1 <= sound_option <= len(sounds):
            sound_file = os.path.join(sound_dir, sounds[sound_option - 1])
        else:
            print("Invalid choice, exiting.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a numeric choice.")
        sys.exit(1)

    duration = duration_minutes * 60
    countdown_timer(duration, repeat, sound_file)

