import os

def main():
    while True:
        print("Choose a option:\n")
        print("1 → wcalc")
        print("2 → percent calculator")
        print("3 → Gear_calculator")
        print("q → end the program")

        choice = input ("Zadejdte vstup: ")

        if choice == '1':
            os.system('wcalc')
        elif choice == '2':
            os.system('python3 percent.py')
        elif choice == '3':
            os.system('python3 Gear_for_Blender.py')
        elif choice == 'q':
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()