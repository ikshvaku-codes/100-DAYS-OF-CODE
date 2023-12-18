#Day 6:- Functions
def sum(a:int, b:int):
    return a + b

def minus(a:int,b:int):
    return a - b
def product(a:int,b:int):
    return a * b

def divisional(a:int, b:int):
    return (a / b) if b != 0 else "Infinity"


while True:
    num1 = int(input("Enter the first digit:- "))
    num2 = int(input("Enter the second digit:- "))
    
    operation = int(input("Select 1 for Addition, 2 for Subtraction, 3 for multiplication, 4 for division"))
    
    print(f'Answer:- {sum(num1, num2) if operation == 1 else minus(num1, num2) if operation == 2 else product(num1, num2) if operation == 3 else divisional(num1, num2)}')
    
    continu = input("Exit/Continue... Type(E/C)")
    
    if continu == 'E':
        break