# Converting between Celsius and Fahrenheit | Royce Chan

def ctof():
    print()

    while True: # While loop (True until a valid integer is given)
        celsius = input("Enter the °C you would like to convert to °F: ")
        try:
            celsius = int(celsius)
            c_fahrenheit = (celsius * 1.8) + 32 # Conversion from °C to °F
            break
        except:
            print("Invalid input!")
            print()
            
    print("-" * 30)
    print(f"{celsius} °C to degrees Fahrenheit is {c_fahrenheit} °F.") # F-string to represent values.
    print("-" * 30)

    menu() # "Restart" the program for ease of access.

def ftoc():
    print()

    while True:
        fahrenheit = input("Enter the °F you would like to convert to °C: ") # °F to °C input
        try:
            fahrenheit = int(fahrenheit)
            c_celsius = (fahrenheit - 32) * 5/9
            c_celsius = round(c_celsius, 1)
            break
        except:
            print("Invalid input!")
            print()

    print("-" * 30)
    print(f"{fahrenheit} °F to degrees Celsius is {c_celsius} °C.") # F-string to represent values.
    print("-" * 30)

    menu() # Same thing as ctof()

def kelvin():
    print("." * 25)

    while True:
        print("Would you like to convert...\n1: To Kelvin\n2: From Kelvin") # First single out of it's a to or from Kelvin conversion
        print()
        to_from = input("Select an index: ")
        try:
            to_from = int(to_from)
            if to_from <= 2 and to_from >= 1:
                break
            else:
                print("Out of range!")
        except:
            print("Invalid index!")
    print()

    if to_from == 1:

        while True:
            print("Would you like to convert...\n1: From Celsius\n2: From Fahrenheit") # If it's to Kelvin, C or F to convert from.
            print()
            cf = input("Select an index: ")
            try:
                cf = int(cf)
                if cf <= 2 and cf >= 1:
                    break
                else:
                    print("Out of range!")
            except:
                print("Invalid index!")
        print("." * 25)

        if cf == 1:
            while True:
                celsius = input("Enter the °C you would like to convert to K: ")
                try:
                    celsius = int(celsius)
                    n_kelvin = celsius + 273.15
                    break
                except:
                    print("Invalid input!")
                    print()

            print("-" * 30)
            print(f"{celsius} °C to Kelvin is {n_kelvin} K.")
            print("-" * 30)

            menu()
            
        if cf == 2:
            while True:
                fahrenheit = input("Enter the °F you would like to convert to K: ")
                try:
                    fahrenheit = int(fahrenheit)
                    n_kelvin = round(((fahrenheit - 32) * 5/9) + 273.15, 2)
                    break
                except:
                    print("Invalid input!")
                    print()

            print("-" * 30)
            print(f"{fahrenheit} °F to Kelvin is {n_kelvin} K.")
            print("-" * 30)

            menu()
            
    else: # Else, C or F to convert to.
        while True:
            print("Would you like to convert...\n1: To Celsius\n2: To Fahrenheit")
            print()
            cf = input("Select an index: ")
            try:
                cf = int(cf)
                if cf <= 2 and cf >= 1:
                    break
                else:
                    print("Out of range!")
            except:
                print("Invalid index!")
        print("." * 25)

        if cf == 1:
            while True:
                kelvin = input("Enter the K you would like to convert to °C: ")
                try:
                    kelvin = int(kelvin)
                    n_celsius = kelvin - 273.15
                    break
                except:
                    print("Invalid input!")
                    print()

            print("-" * 30)
            print(f"{kelvin} K to degrees Celsius is {n_celsius} °C.")
            print("-" * 30)

            menu()
            
        if cf == 2:
            while True:
                kelvin = input("Enter the K you would like to convert to °F: ")
                try:
                    kelvin = int(kelvin)
                    n_fahrenheit = round(((kelvin - 273.15) * 1.8) + 32, 2)
                    break
                except:
                    print("Invalid input!")
                    print()

            print("-" * 30)
            print(f"{kelvin} K to degrees Fahrenheit is {n_fahrenheit} °F.")
            print("-" * 30)

            menu()
    
def ex():
    exit() # Exit function to end program.

def menu():

    # Create a menu with a list as a value, so that the key accesses a function after input.
    menu = {
    "1": [": Convert °C to °F", ctof], # [1] - ctof()
    "2": [": Convert °F to °C", ftoc], # [2] - ftoc()
    "3": [": Convert using Kelvin", kelvin], # [3] - kelvin()
    "4": [": Exit", ex] # [4] - ex()
    }
    bool_index = False

    for key in sorted(menu.keys()):
        print(key + menu[key][0])

    while not bool_index:
        print()
        index = input("Select an index: ")
        try:
            index = int(index)
            if index <= 4 and index >= 1:
                bool_index = True
            else:
                print("Out of range!")
        except:
            print("Invalid index.")

    menu[str(index)][1]()
    
def main():
    print("Welcome to the temperature conversion program.")
    print("-" * 30)

    menu()

if __name__ == "__main__":
    main()
    
