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
