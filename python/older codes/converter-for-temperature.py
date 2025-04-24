choice = input("Enter 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ").upper()

if choice == 'C':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("%.2f Celsius = %.2f Fahrenheit" % (celsius, fahrenheit))
elif choice == 'F':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("%.2f Fahrenheit = %.2f Celsius" % (fahrenheit, celsius))
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
