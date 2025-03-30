import os

def main():
    while True:
        print("Choose an option:")
        print("1. Pomodoro [Sound]")
        print("2. Countdown Timer")
        print("3. Stopwatch")
        print("4. Alarm")
        print("5. Pomodoro [Multiple Alarms]") 
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            os.system('python3 Pomodoro_sound.py')
        elif choice == '2':
            os.system('python3 timer.py')
        elif choice == '3':
            os.system('python3 stopwatch.py')
        elif choice == '4':
            os.system('python3 alarm.py')
        elif choice == '5':
            os.system('python3 Pomodoro_multiple.py')
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

