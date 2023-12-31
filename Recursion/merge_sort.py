"""
Python Script for Merge Sort on a List

This script defines functions `merge` and `mergeSort` to sort a list using the Merge Sort algorithm, a divide-and-conquer sorting technique.
It demonstrates the use of recursion in Python for sorting a list and includes an example of how to use these functions.

Functions:
    merge(l1, l2, l): Merge two sorted sublists (l1 and l2) into a single sorted list (l).
    mergeSort(l): Sorts the list 'l' using the Merge Sort algorithm.
"""

def merge(l1, l2, l):
    """
    Merge two sorted sublists (l1 and l2) into a single sorted list (l).

    The function iteratively compares elements of the two sublists and 
    merges them into a single sorted list.

    Parameters:
    - l1 (list): The first sorted sublist.
    - l2 (list): The second sorted sublist.
    - l (list): The list in which the merged result is to be stored.

    Returns:
    None: The result is stored in 'l'.
    """
    i, j, k = 0, 0, 0
    while len(l1) > i and len(l2) > j:
        if l1[i] < l2[j]:
            l[k] = l1[i]
            i += 1
        else:
            l[k] = l2[j]
            j += 1
        k += 1

    while len(l1) > i:
        l[k] = l1[i]
        i += 1
        k += 1

    while len(l2) > j:
        l[k] = l2[j]
        j += 1
        k += 1

def mergeSort(l):
    """
    Sorts the list 'l' using the Merge Sort algorithm.

    The function recursively divides the list into two halves, sorts each half, 
    and then merges them back together in sorted order.

    Parameters:
    - l (list): The list to be sorted.

    Returns:
    None: The list 'l' is sorted in place.
    """
    if len(l) == 0 or len(l) == 1:
        return
    
    mid = len(l) // 2
    l1 = l[:mid]
    l2 = l[mid:]
    mergeSort(l1)
    mergeSort(l2)
    merge(l1, l2, l)

if __name__ == "__main__":
    # Example usage of the mergeSort function
    list_of_elements = [1, 10, 5, 8, 6, 3, 9, 2, 4, 7]
    mergeSort(list_of_elements)
    print(f"Sorted list: {list_of_elements}")
