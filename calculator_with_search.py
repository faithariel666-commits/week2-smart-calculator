def basic_calculate(first: float, operator: str, second: float) -> float:
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    else:
        raise ValueError("Unsupported operator.")


def solve_for_x(expression: str, target: float) -> float:
    best_x = None
    smallest_difference = float("inf")

    for number in range(-1000, 1001):
        x_value = number / 10
        result = eval(
            expression.replace("x", str(x_value)),
            {"__builtins__": {}}
        )
        difference = abs(result - target)

        if difference < smallest_difference:
            smallest_difference = difference
            best_x = x_value

    return best_x


def equation_solver_menu():
    expression = input("Enter an expression containing x (example: x + 5): ")
    target = float(input("What should the expression equal? "))

    answer = solve_for_x(expression, target)
    print("Answer: x =", answer)


def visualize_search(expression="x + 5", target=12):
    best_x = None
    smallest_difference = float("inf")

    # A smaller range keeps the demonstration from flooding the terminal.
    for number in range(-100, 101):
        x_value = number / 10
        result = eval(
            expression.replace("x", str(x_value)),
            {"__builtins__": {}}
        )
        difference = abs(result - target)

        print("Trying x =", x_value, "| Difference =", difference)

        if difference < smallest_difference:
            smallest_difference = difference
            best_x = x_value

    print("Best answer:", best_x)


def main():
    while True:
        print("\nSMART CALCULATOR")
        print("1. Basic calculation")
        print("2. Equation solver")
        print("3. Search visualization")
        print("4. What is a search algorithm?")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        try:
            if choice == "1":
                first = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ")
                second = float(input("Enter second number: "))
                print("Result:", basic_calculate(first, operator, second))

            elif choice == "2":
                equation_solver_menu()

            elif choice == "3":
                visualize_search()

            elif choice == "4":
                print("A brute-force search tries many possible answers.")
                print("It can be slow because it checks each possibility.")
                print("A smarter approach is algebra, which solves equations directly.")

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose 1 to 5.")

        except (ValueError, ZeroDivisionError, SyntaxError) as error:
            print("Error:", error)
def equation_solver_menu():
        equation = input("Enter an equation (example: x + 5 = 12): ")
        left_side, right_side = equation.split("=")
        target = float(right_side)
        answer = solve_for_x(left_side.strip(), target)
        print("The answer for x is:", answer)
if __name__ == "__main__":
    main()
