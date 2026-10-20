print("===== Simple Calculator =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

choice = input("Enter your choice (1/2/3/4/5): ")

match choice:
    case "1":
        print(f"Result: {num1 + num2}")

    case "2":
        print(f"Result: {num1 - num2}")

    case "3":
        print(f"Result: {num1 * num2}")

    case "4":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed!")

    case "5":
        if num2 != 0:
            print(f"Result: {num1 % num2}")
        else:
            print("Error: Modulus by zero is not allowed!")

    case _:
        print("Invalid choice!")
