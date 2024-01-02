"""
Python Script to Check if a String is a Palindrome Using Recursion

This script defines a function `palindrome` to check whether a given string is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same 
forward and backward (ignoring spaces, punctuation, and capitalization). 
It demonstrates the use of recursion in Python for this purpose and includes an example of how to use the function.

Functions:
    palindrome(string): Check if the string 'string' is a palindrome.
"""

def palindrome(string):
    """
    Check if the string 'string' is a palindrome, using recursion.

    The function compares the first and last characters of the string and 
    recursively checks the remaining substring. 

    Parameters:
    - string (str): The string to be checked.

    Returns:
    bool: True if the string is a palindrome, False otherwise.

    Examples:
    - palindrome("radar") returns True
    - palindrome("python") returns False
    """
    length = len(string)
    if length <= 1:
        return True
    if string[0] != string[length - 1]:
        return False
    return palindrome(string[1:-1])

if __name__ == "__main__":
    # Example usage of the palindrome function
    example_string = "radar"
    print(f"Is '{example_string}' a palindrome? {palindrome(example_string)}")

    example_string = "python"
    print(f"Is '{example_string}' a palindrome? {palindrome(example_string)}")

    # Additional Example
    example_string = "abba"
    print(f"Is '{example_string}' a palindrome? {palindrome(example_string)}")
