"""
Python Script to Find the Last Index of an Element in a List Using Recursion

This script defines a function `last_index` that finds the last index of a specified element in a list, starting the search from a given index, using recursion.
It demonstrates the use of recursion in Python for searching within a list and includes examples of how to use the function.

Functions:
    last_index(a, x, start_index): Find the last index of element 'x' in list 'a' starting from 'start_index'.
"""

def last_index(a, x, start_index):
    """
    Find the last index of element 'x' in list 'a', starting the search from 'start_index', using recursion.

    The function checks each element of the list starting from 'start_index' for equality with 'x'.
    If the element is found, it continues to search the rest of the list to find the last occurrence.
    The base case is when the end of the list is reached, indicated by 'start_index' being equal to the length of the list.

    Parameters:
    - a (list): The list in which to search for the element.
    - x (any): The element to search for in the list.
    - start_index (int): The index in the list from which to start the search.

    Returns:
    int: The index of the last occurrence of 'x' in 'a' starting from 'start_index', or -1 if 'x' is not found.

    Examples:
    - last_index([1, 2, 5, 5, 4], 5, 0) returns 3
    - last_index([1, 2, 3, 4, 5], 6, 0) returns -1
    """
    if start_index == len(a):
        return -1
    smallerListOutput = last_index(a, x, start_index + 1)

    if smallerListOutput != -1:
        return smallerListOutput
    if a[start_index] == x:
        return start_index
    return -1

if __name__ == "__main__":
    # Example usage of the last_index function
    list_elements = [1, 2, 5, 5, 4]
    element_to_find = 5
    print(f"Last index of {element_to_find} in {list_elements} is {last_index(list_elements, element_to_find, 0)}")

    list_elements = [1, 2, 3, 4, 5]
    element_to_find = 6
    print(f"Last index of {element_to_find} in {list_elements} is {last_index(list_elements, element_to_find, 0)}")
