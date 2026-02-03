# task-1
# Function to calculate factorial using a loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Ask number from the user
number = int(input("Enter a number: "))

# Call the function
fact = factorial(number)

# Print the result
print(f"The factorial of {number} is: {fact}")



#task-2
import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Display the results
print(f"Square root of {num}: {square_root}")
print(f"Natural logarithm of {num}: {natural_log}")
print(f"Sine of {num} (in radians): {sine_value}")
