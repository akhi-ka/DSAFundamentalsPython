"""
Python Script for Quick Sort on a List

This script defines functions `partition` and `quickSort` to sort a list using the Quick Sort algorithm, a divide-and-conquer sorting technique.
It demonstrates the use of recursion in Python for sorting a list and includes various examples of how to use these functions.

Functions:
    partition(l, si, ei): Partition the list around a pivot.
    quickSort(l, si, ei): Sorts the list 'l' using the Quick Sort algorithm.
"""

def partition(l, si, ei):
    """
    Partition the list 'l' around a pivot, rearranging elements so that those less than the pivot 
    are on the left, and those greater are on the right.

    Parameters:
    - l (list): The list to be partitioned.
    - si (int): The start index for partitioning.
    - ei (int): The end index for partitioning.

    Returns:
    int: The index position of the pivot after partitioning.

    Example:
    - partition([10, 5, 8, 1, 7, 6], 0, 5) might return 3, with list modified to [5, 1, 6, 7, 8, 10]
    """
    pivot = l[si]
    c = 0
    for i in range(si, ei+1):
        if l[i] < pivot:
            c += 1
    l[si+c], l[si] = l[si], l[si+c]
    pivot_index = si + c

    i = si
    j = ei
    while i < j:
        if l[i] < pivot:
            i += 1
        elif l[j] >= pivot:
            j -= 1
        else:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
    return pivot_index

def quickSort(l, si, ei):
    """
    Sorts the list 'l' using the Quick Sort algorithm.

    Parameters:
    - l (list): The list to be sorted.
    - si (int): The start index for sorting.
    - ei (int): The end index for sorting.

    Returns:
    None: The list 'l' is sorted in place.

    Example:
    - quickSort([10, 5, 8, 1, 7, 6], 0, 5) modifies the list to be sorted.
    """
    if si > ei:
        return

    pivot_index = partition(l, si, ei)
    quickSort(l, si, pivot_index - 1)
    quickSort(l, pivot_index + 1, ei)

if __name__ == "__main__":
    # Example usage of the quickSort function
    list_of_elements = [10, 5, 8, 1, 7, 6]
    quickSort(list_of_elements, 0, len(list_of_elements) - 1)
    print(f"Sorted list: {list_of_elements}")

    # Additional Examples
    example_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    quickSort(example_list, 0, len(example_list) - 1)
    print(f"Sorted list: {example_list}")

    example_list = [20, 5, 15, 10, 0, 25, 30]
    quickSort(example_list, 0, len(example_list) - 1)
    print(f"Sorted list: {example_list}")
