print("Welcome to the calculator app!")

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def power(x, y):
  return x ** y


operation = input("What operation would you like to do? (Add, Subtract, Multiply, Divide, Exponent").title().strip()

firstNum = int(input("Enter a first number): "))
secondNum = int(input("Enter a second number): "))

if operation == "Add":
  print(f"{firstNum} + {secondNum} = {add(firstNum, secondNum)}")
elif operation == "Subtract":
  print(f"{firstNum} - {secondNum} = {subtract(firstNum, secondNum)}")
elif operation == "Multiply":
  print(f"{firstNum} * {secondNum} = {multiply(firstNum, secondNum)}")
elif operation == "Divide":
  print(f"{firstNum} / {secondNum} = {divide(firstNum, secondNum)}")
elif operation == "Exponent":
  print(f"{firstNum} ^ {secondNum} = {power(firstNum, secondNum)}")
else:
  print("Invalid operation. Please try again.")
