def convert_units():
    print("Welcome to Petar's Unit Converter")
    print("1: Convert Kilometers to Miles")
    print("2: Convert Miles to Kilometers")
    print("3: Convert Celsius to Fahrenheit")
    print("4: Convert Fahrenheit to Celsius")
    print("5: Exit")

    while True:
        choice = input("\nEnter the number of your choice: ")

        if choice == '1':
            km = float(input("Enter distance in kilometers: "))
            miles = km * 0.621371
            print(f"{km} kilometers is {miles:.2f} miles.")

        elif choice == '2':
            miles = float(input("Enter distance in miles: "))
            km = miles / 0.621371
            print(f"{miles} miles is {km:.2f} kilometers.")

        elif choice == '3':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is {fahrenheit:.2f}°F.")
        
        elif choice == '4':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is {celsius:.2f}°C.")
        
        elif choice == '5':
            print("Goodbye")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Call the function outside of its definition
convert_units()