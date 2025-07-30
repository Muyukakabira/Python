# Basic Calculator Program

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
    operator_symbol = '+'
elif operation == '-':
    result = num1 - num2
    operator_symbol = '-'
elif operation == '*':
    result = num1 * num2
    operator_symbol = '*'
elif operation == '/':
    if num2 == 0:
        print("Division by zero is not allowed!")
        exit()
    result = num1 / num2
    operator_symbol = '/'
else:
    print("Invalid operation! Please use +, -, *, or /")
    exit()


print(f"{num1} {operator_symbol} {num2} = {result}")

