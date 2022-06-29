import sys

def add(a, b):
    equal = a + b
    return equal

def subtract(a, b):
    equal = a - b
    return equal

def multiply(a, b):
    equal = a * b
    return equal

def divide(a, b):
    equal = a / b
    return equal

def choice(a, b, choose):
    if choose == "add":
        return add(a, b)
    elif choose == "subtract":
        return subtract(a, b)
    elif choose == "multiply":
        return multiply(a, b)
    elif choose == "divide":
        return divide(a, b)  

def get_input():
    a = sys.argv[1]
    b = sys.argv[2]
    choose = sys.argv[3]
    return int(a), int(b), str(choose)

def main():
    try:
        a, b, choose = get_input()
        equal = choice(a, b, choose)
        print(equal)
    except Exception as e:
        print("error")

main()