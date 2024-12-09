# factorial_calculations.py

import math


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


def factorial_of_list(numbers: list) -> list:
    """
    Calculate the factorial of each number in a list.

    Args:
        numbers (list): A list of non-negative integers.

    Returns:
        list: A list containing the factorials of the input numbers.

    Raises:
        ValueError: If any number in the list is negative.
    """
    return [factorial(num) for num in numbers]


def is_factorial_of(n: int, result: int) -> bool:
    """
    Check if a given number is the factorial of some integer.

    Args:
        n (int): The number to check.
        result (int): The potential factorial value.

    Returns:
        bool: `True` if `n` is the factorial of an integer, `False` otherwise.
    """
    i = 0
    fact = 1
    while fact < result:
        i += 1
        fact *= i
    return fact == result


def double_factorial(n: int) -> int:
    """
    Calculate the double factorial of a number.

    Double factorial is the product of all the integers from `n` down to 1 that have the same parity (even or odd) as `n`.

    Args:
        n (int): The number for which to calculate the double factorial.

    Returns:
        int: The double factorial of `n`.

    Raises:
        ValueError: If `n` is a negative number.
    """
    if n < 0:
        raise ValueError("Double factorial is not defined for negative numbers")

    result = 1
    while n > 0:
        result *= n
        n -= 2
    return result


def memoized_factorial(n: int, cache: dict = {}) -> int:
    """
    Calculate the factorial of a number using memoization to optimize performance.

    Args:
        n (int): The number for which to calculate the factorial.
        cache (dict, optional): A cache for storing previously computed factorials.

    Returns:
        int: The factorial of the number.
    """
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return 1
    cache[n] = n * memoized_factorial(n - 1, cache)
    return cache[n]
