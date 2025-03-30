# alarm.py
import os
import time
import threading
from datetime import datetime, timedelta
import pygame

stop_flag = False

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # Play the sound in a loop
    while not stop_flag:
        time.sleep(0.1)
    pygame.mixer.music.stop()

def print_progress_bar(remaining_time, total_time, width=50):
    progress = int((total_time - remaining_time) / total_time * width)
    bar = f"|{'=' * progress}{' ' * (width - progress)}|"
    minutes, seconds = divmod(int(remaining_time), 60)
    print(f"\r{bar} {minutes:02d}:{seconds:02d} remaining", end="")

def alarm_clock(alarm_time, sound_file=None):
    total_time = alarm_time - time.time()
    while True:
        current_time = time.time()
        remaining_time = alarm_time - current_time
        if remaining_time <= 0:
            break
        print_progress_bar(remaining_time, total_time)
        time.sleep(1)

    print("\nAlarm time reached!")
    if sound_file:
        global stop_flag
        stop_flag = False
        sound_thread = threading.Thread(target=play_sound, args=(sound_file,))
        sound_thread.start()
        input("Press Enter to stop the sound and exit...")
        stop_flag = True
        sound_thread.join()

def parse_time_input(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM format.")
        return None

if __name__ == "__main__":
    alarm_time_str = input("Enter the alarm time (HH:MM): ")
    alarm_time = parse_time_input(alarm_time_str)

    if alarm_time is None:
        sys.exit(1)

    now = datetime.now()
    alarm_datetime = datetime.combine(now.date(), alarm_time)

    if alarm_datetime < now:
        alarm_datetime = datetime.combine(now.date() + timedelta(days=1), alarm_time)

    alarm_timestamp = alarm_datetime.timestamp()

    sound_dir = os.path.expanduser("~/Hudba/Budík")
    sounds = [f for f in os.listdir(sound_dir) if f.endswith('.wav') or f.endswith('.mp3')]

    if not sounds:
        print("No sound files found in ~/Hudba/Budík.")
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

    alarm_clock(alarm_timestamp, sound_file)

