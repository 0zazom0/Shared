import os
import time
import pygame
import threading

stop_event = threading.Event()

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # Přehráváme zvuk v loopu
    while not stop_event.is_set():
        time.sleep(0.1)
    pygame.mixer.music.stop()

def print_progress_bar(elapsed_time, total_time, width=50):
    progress = int(elapsed_time / total_time * width)
    bar = f"|{'=' * progress}{' ' * (width - progress)}|"
    remaining_time = int(total_time - elapsed_time)
    minutes, seconds = divmod(remaining_time, 60)
    print(f"\r{bar} {minutes:02d}:{seconds:02d} zbývá", end="")

def multiple_timers(timers):
    while True:
        for index, (name, duration, sound_file) in enumerate(timers):
            print(f"\nOdpočet {index + 1}: {name} ({duration} minut).")
            start_time = time.time()
            while time.time() - start_time < duration * 60:
                elapsed_time = time.time() - start_time
                print_progress_bar(elapsed_time, duration * 60)
                time.sleep(0.1)
            print(f"\r|{'=' * 50}| 00:00 zbývá", end="")
            print(f"\n{name} dokončeno!")

            # Přehrání zvuku
            stop_event.clear()
            sound_thread = threading.Thread(target=play_sound, args=(sound_file,))
            sound_thread.start()
            input("Stiskněte Enter pro zastavení alarmu a pokračování...")
            stop_event.set()
            sound_thread.join()

def prompt_for_sound():
    sound_dir = os.path.expanduser("~/Hudba/Budík")
    sounds = [f for f in os.listdir(sound_dir) if f.endswith('.wav') or f.endswith('.mp3')]

    if not sounds:
        print("Nebyl nalezen žádný zvuk v ~/Hudba/Budík.")
        return None

    print("Vyberte zvuk:")
    for idx, sound in enumerate(sounds, 1):
        print(f"{idx}. {sound}")

    try:
        sound_option = int(input("Zadejte číslo vaší volby: "))
        if 1 <= sound_option <= len(sounds):
            sound_file = os.path.join(sound_dir, sounds[sound_option - 1])
            return sound_file
        else:
            print("Neplatná volba.")
            return None
    except ValueError:
        print("Neplatný vstup.")
        return None

if __name__ == "__main__":
    try:
        # Uživatelské vstupy
        num_timers = int(input("Zadejte počet odpočtů/budíků: "))
        timers = []

        for i in range(num_timers):
            name = input(f"Zadejte název {i + 1}. odpočtu: ")
            duration = float(input(f"Zadejte délku {name} v minutách: "))
            
            # Výběr zvuku pro každý odpočet
            print("\nVyberte zvuk pro tento odpočet:")
            sound_file = prompt_for_sound()
            if sound_file:
                timers.append((name, duration, sound_file))
            else:
                print("Nezvolen žádný zvuk pro tento odpočet. Používám výchozí.")
                timers.append((name, duration, None))

        if not timers:
            print("Nebyl zvolen žádný odpočet.")
            exit()

        print("\nSpouštím odpočty...")
        multiple_timers(timers)

    except ValueError:
        print("Neplatný vstup. Zadejte prosím číselnou hodnotu.")
    except KeyboardInterrupt:
        print("\nProgram byl ukončen uživatelem.")

