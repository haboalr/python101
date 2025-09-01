# my_module.py: used only for importing the functions

def add(a, b):
    """
    This function takes two numbers a and b and returns their sum.
    """
    return a + b


def subtract(a, b):
    """
    This function takes two numbers a and b and returns their difference.
    """
    return a - b


def multiply(a, b):
    """
    This function takes two numbers a and b and returns their product.
    """
    return a * b


def divide(a, b):
    """
    This function takes two numbers a and b and returns their quotient.
    Note: If b is equal to 0, the function returns an error message.
    """
    if b == 0:
        return "Division by zero is not allowed."
    else:
        return a / b
