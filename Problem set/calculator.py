def calculator():
    print("Simple Calculator\n")
    operations = {"1": "Addition", "2": "Subtraction", "3": "Multiplication", "4": "Division", "5": "Modulus"}
    
    for key, value in operations.items():
        print(f"{key}. {value}")
    
    option = input("\nSelect an operation (1-5): ")
    
    if option not in operations:
        print("\nInvalid choice! Please select a valid operation.\n")
        return
    
    try:
        first = int(input("\nEnter first number: "))
        second = int(input("Enter second number: "))
    except ValueError:
        print("\nInvalid input! Please enter numbers only.\n")
        return
    
    print("\nResult:", end=" ")
    
    if option == "1":
        print(f"{first} + {second} = {first + second}\n")
    elif option == "2":
        print(f"{first} - {second} = {first - second}\n")
    elif option == "3":
        print(f"{first} * {second} = {first * second}\n")
    elif option == "4":
        if second == 0:
            print("Error! Division by zero is not allowed.\n")
        else:
            print(f"{first} / {second} = {first / second}\n")
    elif option == "5":
        if second == 0:
            print("Error! Modulus by zero is not allowed.\n")
        else:
            print(f"{first} % {second} = {first % second}\n")

calculator()
