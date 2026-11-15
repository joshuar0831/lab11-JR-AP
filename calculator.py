"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(a)
    except TypeError:
        print("Enter a valid number")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        print("Enter a valid number")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid arguments for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b