"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

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

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero (a cannot be 0)")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Invalid argument for logarithm")
    return math.log(b, a)

def exponent(a, b):
    try:
        return a**b
    except TypeError:
        print("Enter a valid number")







