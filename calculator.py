"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example



# def square_root(a):
#     if a < 0:
#         raise ValueError("Cannot calculate square root of a negative number")
#     return math.sqrt(a)
#
# def hypotenuse(a, b):
#     return math.hypot(a, b)

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid arguments for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b