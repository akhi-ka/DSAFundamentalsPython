"""
Python Script to Calculate the Sum of the First n Natural Numbers Using Recursion

This script defines a function `sum_n` that calculates the sum of the first n natural numbers using a recursive approach.
It demonstrates the use of recursion in Python for a simple arithmetic sum and includes examples of how to use the function.

Functions:
    sum_n(num): Calculate the sum of the first num natural numbers.
"""

def sum_n(num):
    """
    Calculate the sum of the first 'num' natural numbers using recursion.

    The function employs a recursive algorithm where the sum of the first 'n' numbers is defined as:
    sum_n(n) = n + sum_n(n-1)
    The base case for the recursion is when n is 0, where the sum is defined as 0.

    Parameters:
    - num (int): A non-negative integer representing the upper limit of the sum.

    Returns:
    int: The sum of the first 'num' natural numbers.

    Examples:
    - sum_n(5) returns 15
    - sum_n(3) returns 6
    - sum_n(0) returns 0

    Raises:
    - ValueError: If 'num' is a negative integer.
    """
    if num < 0:
        raise ValueError("Input must be a non-negative integer")
    if num == 0:
        return 0
    return num + sum_n(num - 1)

if __name__ == "__main__":
    # Example usage of the function
    try:
        print(f"The sum of the first 5 natural numbers is: {sum_n(5)}")
        print(f"The sum of the first 10 natural numbers is: {sum_n(10)}")
        print(f"The sum of the first 0 natural numbers is: {sum_n(0)}")
        print(f"The sum of the first -1 natural numbers is: {sum_n(-1)}")  # This will raise an exception
    except ValueError as e:
        print(e)
