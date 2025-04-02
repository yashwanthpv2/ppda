def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_converter():
    print("Temperature Converter")
    print("Select the input temperature unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    choice = input("Enter the number corresponding to the input temperature unit: ")

    temperature = float(input("Enter the temperature value to convert: "))

    if choice == '1':  # Celsius
        print(f"{temperature} Celsius is:")
        print(f"{celsius_to_fahrenheit(temperature)} Fahrenheit")
        print(f"{celsius_to_kelvin(temperature)} Kelvin")
    
    elif choice == '2':  # Fahrenheit
        print(f"{temperature} Fahrenheit is:")
        print(f"{fahrenheit_to_celsius(temperature)} Celsius")
        print(f"{fahrenheit_to_kelvin(temperature)} Kelvin")
    
    elif choice == '3':  # Kelvin
        print(f"{temperature} Kelvin is:")
        print(f"{kelvin_to_celsius(temperature)} Celsius")
        print(f"{kelvin_to_fahrenheit(temperature)} Fahrenheit")
    
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

# Call the function to run the converter
temperature_converter()
