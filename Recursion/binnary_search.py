"""
Python Script for Binary Search in a List Using Recursion

This script defines a function `binarySearch` that performs binary search to find the index of a specified element in a sorted list, using recursion.
It demonstrates the use of recursion in Python for searching within a list and includes various examples of how to use the function.

Functions:
    binarySearch(l, a, si, ei): Perform binary search to find the index of element 'a' in list 'l' within the range 'si' to 'ei'.
"""

def binarySearch(l, a, si, ei):
    """
    Perform binary search to find the index of element 'a' in a sorted list 'l', within the range specified by 'si' to 'ei', using recursion.

    The function checks the middle element of the current range. If the element matches 'a', it returns its index. 
    If the element is greater than 'a', it recursively searches the left half of the list. 
    If the element is less than 'a', it recursively searches the right half. 
    The base case is when 'si' exceeds 'ei', indicating the element is not found.

    Parameters:
    - l (list): The sorted list in which to search for the element.
    - a (any): The element to search for in the list.
    - si (int): The start index of the range within the list where the search is to be performed.
    - ei (int): The end index of the range within the list where the search is to be performed.

    Returns:
    int: The index of 'a' in 'l' if found, otherwise -1.

    Examples:
    - binarySearch([1, 2, 3, 4, 5], 3, 0, 4) returns 2
    - binarySearch([1, 2, 3, 4, 5], 6, 0, 4) returns -1
    - binarySearch([10, 20, 30, 40, 50], 40, 0, 4) returns 3
    - binarySearch([1, 3, 5, 7, 9], 8, 0, 4) returns -1
    """
    if si > ei:
        return -1

    mid = (si + ei) // 2
    if l[mid] == a:
        return mid
    elif l[mid] > a:
        return binarySearch(l, a, si, mid - 1)
    else:
        return binarySearch(l, a, mid + 1, ei)

if __name__ == "__main__":
    # Example usage of the binarySearch function
    list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    element_to_find = 8
    print(f"Index of {element_to_find} in {list_of_elements} is {binarySearch(list_of_elements, element_to_find, 0, 9)}")

    # Additional Examples
    list_of_elements = [10, 20, 30, 40, 50]
    element_to_find = 40
    print(f"Index of {element_to_find} in {list_of_elements} is {binarySearch(list_of_elements, element_to_find, 0, 4)}")

    list_of_elements = [1, 3, 5, 7, 9]
    element_to_find = 8
    print(f"Index of {element_to_find} in {list_of_elements} is {binarySearch(list_of_elements, element_to_find, 0, 4)}")



