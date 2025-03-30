import time
import pygame
import os
import threading

stop_event = threading.Event()

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)
    while not stop_event.is_set():
        time.sleep(0.1)
    pygame.mixer.music.stop()

def print_progress_bar(elapsed_time, total_time, width=50):
    progress = int(elapsed_time / total_time * width)
    bar = f"|{'=' * progress}{' ' * (width - progress)}|"
    remaining_time = int(total_time - elapsed_time)
    minutes, seconds = divmod(remaining_time, 60)
    print(f"\r{bar} {minutes:02d}:{seconds:02d} remaining", end="")

def pomodoro_timer(work_duration, break_duration, work_sound_file, break_sound_file):
    while True:
        print(f"Work for {work_duration} minutes.")
        start_time = time.time()
        while time.time() - start_time < work_duration * 60:
            elapsed_time = time.time() - start_time
            print_progress_bar(elapsed_time, work_duration * 60)
            time.sleep(0.1)
        print(f"\r|{'=' * 50}| 00:00 remaining", end="")
        print("\nWork time's up!")

        stop_event.clear()
        sound_thread = threading.Thread(target=play_sound, args=(work_sound_file,))
        sound_thread.start()

        input("Press Enter to stop the alarm and start your break...")
        stop_event.set()
        sound_thread.join()

        print(f"Take a break for {break_duration} minutes.")
        start_time = time.time()
        while time.time() - start_time < break_duration * 60:
            elapsed_time = time.time() - start_time
            print_progress_bar(elapsed_time, break_duration * 60)
            time.sleep(0.1)
        print(f"\r|{'=' * 50}| 00:00 remaining", end="")
        print("\nBreak time's up!")

        stop_event.clear()
        sound_thread = threading.Thread(target=play_sound, args=(break_sound_file,))
        sound_thread.start()

        input("Press Enter to stop the alarm and start working again...")
        stop_event.set()
        sound_thread.join()

if __name__ == "__main__":
    work_duration = float(input("Enter work duration in minutes: "))
    break_duration = float(input("Enter break duration in minutes: "))

    sound_dir = os.path.expanduser("~/Hudba/Budík")
    sounds = [f for f in os.listdir(sound_dir) if f.endswith(('.mp3', '.wav'))]
    
    if not sounds:
        print("No sound files found in ~/Hudba/Budík.")
        sys.exit(1)

    print("Choose a sound for work:")
    for idx, sound in enumerate(sounds, 1):
        print(f"{idx}. {sound}")
    
    try:
        work_sound_option = int(input("Enter your choice: "))
        if 1 <= work_sound_option <= len(sounds):
            work_sound_file = os.path.join(sound_dir, sounds[work_sound_option - 1])
        else:
            print("Invalid choice, exiting.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a numeric choice.")
        sys.exit(1)

    print("Choose a sound for break:")
    for idx, sound in enumerate(sounds, 1):
        print(f"{idx}. {sound}")
    
    try:
        break_sound_option = int(input("Enter your choice: "))
        if 1 <= break_sound_option <= len(sounds):
            break_sound_file = os.path.join(sound_dir, sounds[break_sound_option - 1])
        else:
            print("Invalid choice, exiting.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a numeric choice.")
        sys.exit(1)

    pomodoro_timer(work_duration, break_duration, work_sound_file, break_sound_file)

