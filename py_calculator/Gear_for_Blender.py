import os
def Gear_for_Blender():

    # Definition
    print("""
    Dedendum mění skutečný radius bez závislosti na adendu a dedendu.
    Adendum se přičítá ke skutečnému dedendu.
    Radius stahuje Adendum i dedendum.
    ↑Diff↑ → ↓skutečný radius a dedendum↓ ↑Adendum↑.
    ↑DiffR↑ → ↓skutečný radius menší↓.\n
    """)
    print("Enter 'q' to quit\n")
    
    while True:
        # Input
        # teeth
        teeth = input("teeth: ").strip()
        if teeth.lower() == 'q':
            return
        try:
            teeth = int(teeth)
            if teeth <= 0:
                print("Invalid input")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # hole
        hole = input("hole: ").strip()
        if hole.lower() == 'q':
            return
        try:
            hole = float(hole)
            if hole <= 0:
                print("Invalid input")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # diameter
        diameter = input("Ø: ").strip()
        if diameter.lower() == 'q':
            return
        try:
            diameter = float(diameter)
            if diameter <= 0:
                print("Invalid input")
                print("Input shall not be lower than 0\n")
                continue
            if diameter <= hole:
                print("Invalid input")
                print("Input shall not be lower or equal to hole\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # Gear
        Gear = input("Gear: ").strip()
        if Gear.lower() == 'q':
            return
        try:
            Gear = float(Gear)
            if Gear <= 0 :
                print("Invalid input")
                print("Input shall not be lower than 0\n")
                continue
            if Gear <= hole:
                print("Invalid input")
                print("Input shall not be lower or equal to hole\n")
                continue
            if Gear <= diameter:
                print("Invalid input")
                print("Input shall not be lower or equal to diameter\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # width
        width_input = input("width_input: ").strip()
        if width_input.lower() == 'q':
            return
        try:
            width_input = float(width_input)
            if width_input <= 0 :
                print("Invalid input")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # Diffr
        DiffR = input("DiffR: ").strip()
        if DiffR.lower() == 'q':
            return
        try:
            DiffR = float(DiffR)
        except ValueError:
            print("Invalid input\n")
            continue
        # Diff
        Diff = input("Diff: ")
        if Diff.lower() == 'q':
            return
        try:
            Diff = float(Diff)
        except ValueError:
            print("Invalid input\n")
            continue


        # Calculations
        width = width_input / 2
        Base =( diameter - hole) / 2
        Addendum = diameter / teeth
        Dedendum = Addendum * 1.25 + DiffR if DiffR != 0 else Addendum * 1.25
        #° Radius = (Gear / 2) - Dedendum

        if Diff > 0:
            Addendum += (Diff)
            Radius -= (Diff)
        elif Diff < 0:
            Addendum -= abs(Diff)
            Radius += abs(Diff)
        else:
            Addendum += (Diff)
            Radius += (Diff)

        # Results
        print("\nResults:\n")
        print(f"Number of teeth → {teeth:}")
        print(f"Radius → {Radius:.3f}")
        print(f"width → {width:.3f}")
        print(f"Base → {Base:.3f}")
        print(f"Dedendum → {Dedendum:.3f}")
        print(f"Addendum → {Addendum:.3f}\n")
if __name__ == "__main__":
    Gear_for_Blender()