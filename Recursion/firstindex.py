"""
Python Script to Find the First Index of an Element in a List Using Recursion

This script defines a function `first_index` that finds the first index of a specified element in a list, starting the search from a given index, using recursion.
It demonstrates the use of recursion in Python for searching within a list and includes examples of how to use the function.

Functions:
    first_index(a, x, start_index): Find the first index of element 'x' in list 'a' starting from 'start_index'.
"""

def first_index(a, x, start_index):
    """
    Find the first index of element 'x' in list 'a', starting the search from 'start_index', using recursion.

    The function checks each element of the list starting from 'start_index' for equality with 'x'.
    If the element is found, it returns the index, otherwise, it recursively calls itself with the next index.
    The base case is when the end of the list is reached, indicated by 'start_index' being equal to the length of the list.

    Parameters:
    - a (list): The list in which to search for the element.
    - x (any): The element to search for in the list.
    - start_index (int): The index in the list from which to start the search.

    Returns:
    int: The index of the first occurrence of 'x' in 'a' starting from 'start_index', or -1 if 'x' is not found.

    Examples:
    - first_index([1, 2, 3, 4, 5], 3, 0) returns 2
    - first_index([1, 2, 3, 4, 5], 6, 0) returns -1
    """
    if start_index == len(a):
        return -1
    if a[start_index] == x:
        return start_index
    return first_index(a, x, start_index + 1)

if __name__ == "__main__":
    # Example usage of the first_index function
    list_elements = [1, 2, 3, 4, 5]
    element_to_find = 3
    print(f"First index of {element_to_find} in {list_elements} is {first_index(list_elements, element_to_find, 0)}")

    list_elements = [1, 2, 3, 4, 5]
    element_to_find = 6
    print(f"First index of {element_to_find} in {list_elements} is {first_index(list_elements, element_to_find, 0)}")
