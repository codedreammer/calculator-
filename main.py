print("Welcome to the Python Calculator!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    if choice == '1':
            print(f"{num1} + {num2} = {(num1, num2)}")
    elif choice == '2':
            print(f"{num1} - {num2} = {(num1, num2)}")
    elif choice == '3':
            print(f"{num1} * {num2} = {(num1, num2)}")
    elif choice == '4':
            print(f"{num1} / {num2} = {(num1, num2)}")
    else:
        print("Invalid input. Please select a valid operation.")

