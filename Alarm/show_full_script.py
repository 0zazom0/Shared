import os

# Seznam všech souborů, které chceme zobrazit
files_to_show = [
    'main.py',
    'alarm.py',
    'stopwatch.py',
    'test_sound.py',
    'timer.py',
    'Pomodoro_sound.py',
    'Pomodoro_multiple.py'
]

def show_combined_files(files):
    for fname in files:
        if os.path.exists(fname):
            with open(fname, 'r') as f:
                print(f"# {fname}")
                print(f.read())
                print("\n" + "#" * 80 + "\n")
        else:
            print(f"# {fname} not found.\n")

if __name__ == "__main__":
    show_combined_files(files_to_show)
