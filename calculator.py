"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid logarithm argument")
    return math.log(b, a)

def exp(a, b):
    return a ** b


import math

# def square_root(a):
#     if a < 0:
#         raise ValueError("Cannot calculate square root of a negative number")
#     return math.sqrt(a)
#
# def hypotenuse(a, b):
#     return math.hypot(a, b)

def add(a, b):
    try:
        return a+b
    except TypeError:
        print("Enter a valid number")

def subtract(a, b):
    try:
        return a-b
    except TypeError:
        print("Enter a valid number")

def multiply(a, b):
    try:
        return a*b
    except TypeError:
        print("Enter a valid number")

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Invalid argument for logarithm")
    return math.log(b, a)

def exponent(a, b):
    try:
        return a**b
    except TypeError:
        print("Enter a valid number")





