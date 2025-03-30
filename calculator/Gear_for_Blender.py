import os
def Gear_for_Blender():

    # Výpis definice na začátek
    print("""
    Dedendum mění skutečný radius bez závislosti na adendu a dedendu.
    Adendum se přičítá ke skutečnému dedendu.
    Radius stahuje Adendum i dedendum.
    ↑Diff↑ → ↓skutečný radius a dedendum↓ ↑Adendum↑.
    ↑DiffR↑ → ↓skutečný radius menší↓.\n
    """)
    print("Enter an expression to evaluate 'q' to quit\n")
    
    while True:
        # Vstupní hodnoty
        # teeth
        teeth = input("teeth: \n").strip()
        if teeth.lower() == 'q':
            return
        try:
            teeth = int(teeth)
            if teeth <= 0:
                print("Invalid input\n")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # hole
        hole = input("hole: \n").strip()
        if hole.lower() == 'q':
            return
        try:
            hole = float(hole)
            if hole <= 0:
                print("Invalid input\n")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # diameter
        diameter = input("Ø: \n").strip()
        if diameter.lower() == 'q':
            return
        try:
            diameter = float(diameter)
            if diameter <= 0:
                print("Invalid input\n")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # Gear
        Gear = input("Gear: \n").strip()
        if Gear.lower() == 'q':
            return
        try:
            Gear = float(Gear)
            if Gear <= 0:
                print("Invalid input\n")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # Diffr
        DiffR = input("DiffR: \n").strip()
        if DiffR.lower() == 'q':
            return
        try:
            DiffR = float(DiffR)
            if DiffR <= 0:
                print("Invalid input\n")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue
        # Diff
        Diff = input("Diff: \n").strip()
        if Diff.lower() == 'q':
            return
        try:
            Diff = float(Diff)
            if Diff <= 0:
                print("Invalid input\n")
                print("Input shall not be lower than 0\n")
                continue
        except ValueError:
            print("Invalid input\n")
            continue

        # Mazání vstupů (6 řádků + 1 prázdný)
        print("\033[F"*7 + "\033[K"*7, end="")

        # Výpočty
        Base =( diameter - hole) / 2
        Addendum = diameter / teeth
        Dedendum = Addendum * 1.25 + DiffR if DiffR != 0 else Addendum * 1.25
        Radius = (diameter / 2) + Dedendum

        if Diff > 0:
            Addendum += (Diff)
            Radius -= (Diff)
        elif Diff < 0:
            Addendum -= abs(Diff)
            Radius += abs(Diff)
        else:
            Addendum += (Diff)
            Radius += (Diff)

        # Výpis výsledků
        print("\nVýsledné hodnoty:\n")
        print(f"Number of teeth → {teeth:}\n")
        print(f"Radius → {Radius:.3f}\n")
        print(f"Base → {Base:.3f}\n")
        print(f"Dedendum → {Dedendum:.3f}\n")
        print(f"Addendum → {Addendum:.3f}\n")
if __name__ == "__main__":
    Gear_for_Blender()