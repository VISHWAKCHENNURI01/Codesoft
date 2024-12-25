# %%
#Task2:Simple Calculator 
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter your choice of operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation choice. Please try again.")
            return
        
        print(f"The result of {num1} {operation} {num2} is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        
calculator()


