"""
Python Script to Check if a List is Sorted in Ascending Order Using Recursion

This script defines a function `isSorted` that checks whether a list of elements is sorted in ascending order using a recursive approach.
It demonstrates the use of recursion in Python for checking the order of elements in a list and includes examples of how to use the function.

Functions:
    isSorted(a): Check if a given list is sorted in ascending order.
"""

def isSorted(a):
    """
    Check if a given list is sorted in ascending order using recursion.

    The function recursively checks if each element in the list is less than or equal to its next element.
    The base cases are when the list is empty or contains only one element, where it's considered sorted.

    Parameters:
    - a (list): A list of elements (typically numbers) to check for sorting.

    Returns:
    bool: Returns True if the list is sorted in ascending order, False otherwise.

    Examples:
    - isSorted([1, 2, 3, 4, 5]) returns True
    - isSorted([1, 2, 5, 3, 4]) returns False
    - isSorted([]) returns True
    """
    length = len(a)
    if length == 0 or length == 1:
        return True
    if a[0] > a[1]:
        return False
    return isSorted(a[1:])

if __name__ == "__main__":
    # Example usage of the isSorted function
    list_elements = [1, 2, 3, 4, 5]
    print(f"Is the list {list_elements} sorted? {isSorted(list_elements)}")

    list_elements = [1, 2, 5, 3, 4]
    print(f"Is the list {list_elements} sorted? {isSorted(list_elements)}")

    list_elements = []
    print(f"Is the list {list_elements} sorted? {isSorted(list_elements)}")
