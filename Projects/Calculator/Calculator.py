from art import clear, logo

def add(a,b):
    return a+b

def sub(a,b):
    return(a-b)

def div(a,b):
    return a/b

def multi(a,b):
    return a*b

operations={"+": add, "-": sub, "*": multi, "/": div}

def calci():
    num1=float(input("Enter first number:"))
    again=True
    while again:
        for op in operations:
            print(op)
        operation=input("Pick an operation:")
        num2=float(input("Enter second number:"))
        if operation in operations:
            cal_func=operations[operation]
        else:
            print("Enter a valid operation....")
            return
        answer=cal_func(num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1=answer
        else:
            again=False
            clear()
            calci()
    
calci()