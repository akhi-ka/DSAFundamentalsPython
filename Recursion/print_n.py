"""
Python Script to Print the First n Natural Numbers Using Recursion

This script defines a function `print_one_to_n` that prints the first n natural numbers in ascending order using a recursive approach.
It demonstrates the use of recursion in Python for iterating through a range of numbers and includes an example of how to use the function.

Functions:
    print_one_to_n(num): Print the first num natural numbers in ascending order.
"""

def print_one_to_n(num):
    """
    Print the first 'num' natural numbers in ascending order using recursion.

    This function uses a recursive approach to print numbers from 1 to 'num'.
    It first counts down to the base case (0) and then prints the numbers in ascending order
    as the recursive calls return.

    Parameters:
    - num (int): A non-negative integer indicating the number of natural numbers to print.

    Returns:
    None: This function does not return a value; it prints numbers to the console.

    Examples:
    - print_one_to_n(5) prints 1, 2, 3, 4, 5

    Raises:
    - ValueError: If 'num' is a negative integer.
    """
    if num < 0:
        raise ValueError("Input must be a non-negative integer")
    if num == 0:
        return
    print_one_to_n(num - 1)
    print(num)

if __name__ == "__main__":
    # Example usage of the function
    try:
        num = 10
        print("Printing the first 5 natural numbers:")
        print_one_to_n(num)
    except ValueError as e:
        print(e)
