# Project 1: Calculator
# Console calculator, operations +, -, *, /


def get_number(prompt):
    # input validation - keep asking until we get a real number
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_operation():
    # only these 4 operations are allowed
    valid_operations = ["+", "-", "*", "/"]
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        print("Invalid operation! Please choose +, -, * or /.")


def calculate(a, b, operation):
    # does the math depending on which operation was picked
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:  # can't divide by zero
            return None
        return a / b


def main():
    # main loop - keeps calculating until the user says no
    print("=== Simple Calculator ===")

    while True:
        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")
        operation = get_operation()

        result = calculate(first_number, second_number, operation)
        if result is None:
            print("Error: division by zero is not allowed!")
        else:
            print(f"Result: {first_number} {operation} {second_number} = {result}")

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            break


if __name__ == "__main__":
    main()
