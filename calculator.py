"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(a, b)

def exp(a, b):
    return a ** b




