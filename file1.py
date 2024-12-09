# math_calculations.py

import math

def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract the second number from the first number.

    Args:
        a (float): The number from which to subtract.
        b (float): The number to subtract.

    Returns:
        float: The difference between the two numbers.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide the first number by the second number.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient.

    Raises:
        ZeroDivisionError: If the second number is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """
    Raise the first number to the power of the second number.

    Args:
        a (float): Base number.
        b (float): Exponent.

    Returns:
        float: The result of raising `a` to the power of `b`.
    """
    return math.pow(a, b)


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the number.

    Raises:
        ValueError: If the number is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)


def sqrt(a: float) -> float:
    """
    Calculate the square root of a number.

    Args:
        a (float): The number to calculate the square root of.

    Returns:
        float: The square root of `a`.

    Raises:
        ValueError: If `a` is negative.
    """
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


def sin(angle: float) -> float:
    """
    Calculate the sine of an angle (in radians).

    Args:
        angle (float): The angle in radians.

    Returns:
        float: The sine of the angle.
    """
    return math.sin(angle)


def cos(angle: float) -> float:
    """
    Calculate the cosine of an angle (in radians).

    Args:
        angle (float): The angle in radians.

    Returns:
        float: The cosine of the angle.
    """
    return math.cos(angle)


def tan(angle: float) -> float:
    """
    Calculate the tangent of an angle (in radians).

    Args:
        angle (float): The angle in radians.

    Returns:
        float: The tangent of the angle.
    """
    return math.tan(angle)

def test1():
    """
    New function added successfully

    :return:
    """
    pass
