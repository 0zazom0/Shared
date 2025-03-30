def percent():
    print("Enter an expression to evaluate 'q' to quit\n")
    while True:
        # Inputs
            major = input("Major number: ").strip()
            if major.lower() == 'q':
                 return
            
            try:
                major = int(major)
                if major <= 0:
                    print("Invalid input\n")
                    continue
            except ValueError:
                print("Invalid input\n")
                continue

            minor = input("Minor number: ").strip()
            if minor.lower() == 'q':
                 return
            
            try:
                 minor = int(minor)
                 if minor <= 0:
                      print ("Invalid input\n")
                      continue
            except ValueError:
                print("Invalid input\n")
                continue
            if minor > major:
                 print("Invalid input (Minor input is highter than Major input\n)")
                 continue
            
            # Calculations
            output = (minor / major) * 100
             # Output
            print(f"= {output:.1f}%\n")

if __name__ == "__main__":
    percent()