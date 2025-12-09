def sum(first,second):
    result = first + second
    return result
def minus(first,second):
    return first - second
def multiply(first,second):
    return first * second
def division(first,second):
    return first / second

return_calculator = False
if return_calculator == False:
    first_n = float(input("What's first number? "))
def home():
    global first_n
    global return_calculator
    print("+\n-\n*\n/")
    op = input("Pick an Operation: ")
    second_n = float(input("What's next number? "))
    first_n = float(first_n)
    second_n = float(second_n)
    match op:
        case "+":
            result = sum(first_n,second_n)
            print(f"{first_n} + {second_n} = {result}")    
        case "-":
            result = minus(first_n,second_n)
            print(f"{first_n} - {second_n} = {result}")    
        case "*":
            result = multiply(first_n,second_n)
            print(f"{first_n} * {second_n} = {result}")    
        case "/":
            result = division(first_n,second_n)
            print(f"{first_n} / {second_n} = {result}")    
    next = input(f"Type 'y' to continue calculationg with {result}, or type 'n' to start a new calculation: ")
    if next.lower() == "y":
        first_n = result
        return_calculator = True
        home()
    else:
        return_calculator = False
        home()
home()