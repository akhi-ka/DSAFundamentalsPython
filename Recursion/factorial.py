
"""
Python Script to Calculate Factorial of a Number Using Recursion

This script defines a function `factorial` that calculates the factorial of a non-negative integer using a recursive approach.
It demonstrates the use of recursion in Python and includes examples of how to use the function.

Functions:
    factorial(num): Calculate the factorial of a given non-negative integer.
"""

def factorial(num):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    The function uses a basic recursive algorithm where the factorial of a number is defined as:
    factorial(n) = n * factorial(n-1)
    The base case for the recursion is when n is 0, where factorial(0) is defined as 1.

    Parameters:
    - num (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given number.

    Examples:
    - factorial(3) returns 6
    - factorial(5) returns 120
    - factorial(0) returns 1

    Raises:
    - ValueError: If 'num' is a negative integer.
    """
    if num < 0:
        raise ValueError("Negative numbers do not have factorials")
    if num == 0:
        return 1
    return num * factorial(num - 1)

if __name__ == '__main__':
    # Example usage of the factorial function
    try:
        print(f"Factorial of 6 is {factorial(6)}")
        print(f"Factorial of 3 is {factorial(3)}")
        print(f"Factorial of 5 is {factorial(5)}")
        print(f"Factorial of 0 is {factorial(0)}")
        print(f"Factorial of -1 is {factorial(-1)}")  # This will raise an exception
    except ValueError as e:
        print(e)
