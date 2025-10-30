def calculator():
    try:
        firstNumber = float(input("Enter first number: "))
        secondNumber = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            result = firstNumber + secondNumber
        elif operator == "-":
            result = firstNumber - secondNumber
        elif operator == "*":
            result = firstNumber * secondNumber
        elif operator == "/":
            if secondNumber == 0:
                print("Error: You cannot divide by zero.")
                return
            result = firstNumber / secondNumber
        else:
            print("Error: Invalid operator.")
            return

        print("Result:", result)

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

calculator()