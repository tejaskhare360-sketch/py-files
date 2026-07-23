# Simple Calculator
print("=" * 30)
print("      SIMPLE CALCULATOR")
print("=" * 30)

while True:
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("\nThanks for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"\nResult: {num1} × {num2} = {result}")

        elif choice == "4":
            if num2 == 0:
                print("\nError! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} ÷ {num2} = {result}")

    except ValueError:
        print("\nPlease enter valid numbers.")
