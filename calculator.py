# https://github.com/vsajinu/lab11-JN-FB/tree/main
# Partner 1: Jimmy Nguyen
# Partner 2: Fred Bertil

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):

    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    
    return math.sqrt(a)


def hypotenuse(a, b):

    return math.hypot(a, b)

def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def mul(a, b):

    return a * b

def div(a, b):

    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (a can't be 0)")
    
    return b / a

def logarithm(a, b):

    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1")
    
    if b <= 0:
        raise ValueError("Log argument must be positive")
    
    return math.log(b, a)

def exp(a, b):

    return a ** b