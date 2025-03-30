# stopwatch.py
import time

def stopwatch():
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            print(f"\rElapsed time: {minutes:02d}:{seconds:02d}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped!")

if __name__ == "__main__":
    stopwatch()

