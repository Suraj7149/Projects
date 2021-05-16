loop = True


def calc(operation):
    if operation.lower() == "add":
        number1 = int(input("Enter the number1:- "))
        number2 = int(input("Enter the number2:- "))
        print("")
        print(number2 + number1)

    elif operation.lower() == "subtract":
        number1 = int(input("Enter the number1:- "))
        number2 = int(input("Enter the number2:- "))
        print("")
        print(number1 - number2)

    elif operation.lower() == "multiply":
        number1 = int(input("Enter the number1:- "))
        number2 = int(input("Enter the number2:- "))
        print("")
        print(number2 * number1)

    elif operation.lower() == "divide":
        number1 = int(input("Enter the number1:- "))
        number2 = int(input("Enter the number2:- "))
        print("")
        print(number1 / number2)
    else:
        print("wrong input.\n")


while loop:
    print("Select an operation to perform: ")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. Exit")

    choice = input("Enter the choice:- ")

    if choice.lower() == "exit":
        break

    else:
        calc(choice)
        continue
