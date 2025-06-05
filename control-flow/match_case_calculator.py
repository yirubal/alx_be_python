num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Choose the operation (+, -, *, /): ")

match op:
    case '+':
        print("The result is", num1 + num2)
    case '-':
        print("The result is", num1 - num2)
    case '*':
        print("The result is", num1 * num2)
    case '/':
        if num2 == 0:
            print("cannot divide by zero.")
        else:
            print("The result is", num1 / num2)
    case _:
        print("Invalid operation")