
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Find the largest number
largest = max(numbers)

# Display the result
print(f"The largest number is: {largest}")
