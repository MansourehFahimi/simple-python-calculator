import math


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a ,b):
    return a*b
def divide(a,b):
    if b==0:
      return "It's not possible to divide by zero"
    return a/b
def power(a,b):
    return a**b
def mod(a,b):
    return a%b
def int_div(a,b):
    if b==0:
      return "It's not possible to divide by zero"
    return a//b
def sqrt(a):
    if a<0:
        return "The square root of a negative number does not exist."
    return math.sqrt(a)


print("Simple Calculator")
print("Operations: + , _ , * , / , ^ , % , // , sqrt ")

operation= input("Enter your operation: ")

if operation == "sqrt":
    a = float(input("Enter your number: "))
    print("Answer: ", sqrt(a))
elif operation in ['+', '-', '*', '/', '^', '%', '//'] :
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))

    if operation == "+":
      print("Answer :", add(a,b))
    elif operation == "-":
      print("Answer :", subtract(a,b))
    elif operation == "*":
      print("Answer :", multiply(a,b))
    elif operation == "/":
      print("Answer :", divide(a,b))
    elif operation == "^":
      print("Answer :", power(a,b))
    elif operation == "%" :
      print("Answer :", mod(a,b))
    elif operation == "//" :
      print("Answer :", int_div(a,b))
    else:
      print("This operation does not available in this simple calculator!")


