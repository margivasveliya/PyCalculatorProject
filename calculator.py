def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Can't divide by zero."
    return a / b

#Main Function
def main():
    print("--Calculator--")
    print("use +  -  *  /")
    print("Type 'e' anytime to exit\n")

    #this loop will run until user decides to exit
    while True:
        operation = input("Choose Operation: (+, -, *, /) or 'e' to quit: ").strip()

        if operation.lower() == 'e':         #if user wants to quit
            print("Bye")
            break

        if operation not in ['+', '-', '*', '/']:
            print("not a valid input,choose again.\n")
            continue

        try:                                         #input the numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Only Numbers are allowed!\n")
            continue

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        #result
        print(f"Result: {result}\n")

    
    
if __name__ == "__main__":
    main()

