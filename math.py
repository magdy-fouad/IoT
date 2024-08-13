# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Getting user input for addition
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
print("The result of addition is:", add(num1, num2))

# Getting user input for subtraction
num1 = float(input("Enter the first number for subtraction: "))
num2 = float(input("Enter the second number for subtraction: "))
print("The result of subtraction is:", subtract(num1, num2))

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Example usage
num1 = 10
num2 = 5

# Multiplication
result_multiply = multiply(num1, num2)
print(f"{num1} * {num2} = {result_multiply}")

# Division
result_divide = divide(num1, num2)
print(f"{num1} / {num2} = {result_divide}")

