#Calculator

def calculator():
    numbers = []
    while True:
        num = input("Enter a number (or 'q' to quit): ")
        if num == 'q':
            break
        try:
            numbers.append(float(num))
        except ValueError:
            print("Invalid input, Please enter a number.")

        operator = input("Enter an operator (+, -, *, /): ")

        result = numbers[0]
        for i in range(1, len(numbers)):
            if operator == "+":
                result += numbers[i]
            elif operator == "-":
                result -= numbers[i]
            elif operator == "*":
                result *= numbers[i]
            elif operator == "/":
                try:
                    result /= numbers[i]
                except ZeroDivisionError:
                    print("Division by zero error!")
            else:
                print("Invalid operator!")
                return

    print("\n Result: ", result)

calculator()