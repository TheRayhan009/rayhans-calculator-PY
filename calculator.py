def calculator(a, sine, b, ans=0):
    x = int(a)
    y = int(b)
    if sine == "+":
        return x + y
    elif sine == "-":
        return x - y
    elif sine == "x":
        return x * y
    elif sine == "/":
        return x / y
    elif sine == "^":
        return x ** y
    elif sine == "%":
        return x % y


def calculator2(sine, b, ans):
    b = int(b)
    if sine == "+":
        return ans + b
    elif sine == "-":
        return ans - b
    elif sine == "*":  # Change "ans" to "*" for multiplication
        return ans * b
    elif sine == "/":
        return ans / b
    elif sine == "^":
        return ans ** b
    elif sine == "%":
        return ans % b

    


def rul():
    print("--------------------------------------------------------------------------------------------------")
    print("enter the first number. then add sine(+ , - , * , / , ^ , % ).then enter the second number.")
    print("1. \" + \" means submission. ")
    print("2. \" - \" means subtraction. ")
    print("3. \" x \" means multiplication. ")
    print("4. \" / \" means division. ")
    print("5. \" ^ \" means pawor.")
    print("6. \" % \" means remainder.")
    print("like: 4")
    print("+ 1")
    print("+ 1")
    print("+ 1")
    print("+ 1")
    print("6. \" % \" means remainder.")
    print("--------------------------------------------------------------------------------------------------")
def want():
    print("How many numbers do you want to count?")
