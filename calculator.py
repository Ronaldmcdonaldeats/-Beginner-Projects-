def add(x, y):
    return x + y

def subtract(x, y):  # fixed spelling
    return x - y

def multiply(x, y):  # fixed spelling
    return x * y

def divide(x, y):  # fixed spelling
    if y == 0:
        return "Cannot divide by 0"
    return x / y

while True:
    print("\nOptions: +, -, *, /, exit")
    op = input("Choose an operation: ")

    if op == "exit":  # fixed condition
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        continue

    if op == "+":
        print(add(num1, num2))
    elif op == "-":
        print(subtract(num1, num2))
    elif op == "*":
        print(multiply(num1, num2))
    elif op == "/":
        print(divide(num1, num2))
    else:
        print("Invalid operation.")
