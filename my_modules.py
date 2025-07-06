# Simple Python Functions

# 1. Text Reverser Function
def reverse_text(text):
    """
    Reverses the given text.
    :param text: str
    :return: str
    """
    return text[::-1]


# 2. Basic Calculator Function
def calculator(a, b, operation):
    """
    Performs basic arithmetic operations.
    :param a: float
    :param b: float
    :param operation: str - one of 'add', 'subtract', 'multiply', 'divide'
    :return: float or str (if error)
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unknown operation"


# 3. Area Calculator Function
def area_calculator(shape, dimension1, dimension2=None):
    """
    Calculates area for basic shapes.
    :param shape: str - 'rectangle', 'triangle', or 'circle'
    :param dimension1: float
    :param dimension2: float (not needed for circle)
    :return: float or str (if error)
    """
    import math
    if shape == 'rectangle':
        return dimension1 * dimension2
    elif shape == 'triangle':
        return 0.5 * dimension1 * dimension2
    elif shape == 'circle':
        return math.pi * dimension1 ** 2
    else:
        return "Error: Unknown shape"


# Example usage (uncomment to test)
# print(reverse_text("Hello"))
# print(calculator(10, 5, 'add'))
# print(area_calculator('circle', 7))
