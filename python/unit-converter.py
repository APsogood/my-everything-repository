def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Unit Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        km = float(input("Enter kilometers: "))
        print(f"{km} kilometers is {km_to_miles(km)} miles.")
    elif choice == '2':
        miles = float(input("Enter miles: "))
        print(f"{miles} miles is {miles_to_km(miles)} kilometers.")
    elif choice == '3':
        kg = float(input("Enter kilograms: "))
        print(f"{kg} kilograms is {kg_to_pounds(kg)} pounds.")
    elif choice == '4':
        pounds = float(input("Enter pounds: "))
        print(f"{pounds} pounds is {pounds_to_kg(pounds)} kilograms.")
    elif choice == '5':
        celsius = float(input("Enter Celsius: "))
        print(f"{celsius} degrees Celsius is {celsius_to_fahrenheit(celsius)} degrees Fahrenheit.")
    elif choice == '6':
        fahrenheit = float(input("Enter Fahrenheit: "))
        print(f"{fahrenheit} degrees Fahrenheit is {fahrenheit_to_celsius(fahrenheit)} degrees Celsius.")
    else:
        print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
