"""
Python Script to Calculate Fibonacci Numbers Using Recursion

This script defines a function `fibonacci` that calculates the n-th number in the Fibonacci sequence using a recursive approach.
It demonstrates the use of recursion in Python to solve a classic mathematical problem and includes examples of how to use the function.

Functions:
    fibonacci(num): Calculate the n-th number in the Fibonacci sequence.
"""

def fibonacci(num):
    """
    Calculate the n-th number in the Fibonacci sequence using recursion.

    The Fibonacci sequence is a series where each number is the sum of the two preceding ones, usually starting with 1 and 1.
    The function uses a recursive approach where the n-th Fibonacci number is defined as:
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    The base cases are when n is 1 or 2, both returning 1.

    Parameters:
    - num (int): A positive integer indicating the position in the Fibonacci sequence.

    Returns:
    int: The n-th number in the Fibonacci sequence.

    Examples:
    - fibonacci(3) returns 2
    - fibonacci(5) returns 5
    - fibonacci(6) returns 8

    Raises:
    - ValueError: If 'num' is not a positive integer.
    """
    if num <= 0:
        raise ValueError("Input must be a positive integer")
    if num == 1 or num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == '__main__':
    # Example usage of the fibonacci function
    try:
        print(f"The 6th Fibonacci number is {fibonacci(6)}")
        print(f"The 3rd Fibonacci number is {fibonacci(3)}")
        print(f"The 5th Fibonacci number is {fibonacci(5)}")
        print(f"The 0th Fibonacci number is {fibonacci(0)}")  # This will raise an exception
    except ValueError as e:
        print(e)
