def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def modulus(x, y):
    """Returns the modulus of two numbers."""
    if y == 0:
        return "Cannot perform modulus with zero divisor"
    return x % y

def exponentiate(x, y):
    """Raises x to the power of y."""
    return x ** y

def floor_divide(x, y):
    """Performs floor division on two numbers."""
    if y == 0:
        return "Cannot perform floor division by zero"
    return x // y

print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Modulus (%)")
print("6. Exponentiation (**)")
print("7. Floor Division (//)")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            result = modulus(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(num1, "%", num2, "=", result)

        elif choice == '6':
            print(num1, "**", num2, "=", exponentiate(num1, num2))

        elif choice == '7':
            result = floor_divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(num1, "//", num2, "=", result)

        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            break
    else:
        print("Invalid input. Please enter a number between 1 and 7.")