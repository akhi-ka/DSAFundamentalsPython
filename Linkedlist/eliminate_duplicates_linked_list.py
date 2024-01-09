"""
Python Script to Eliminate Consecutive Duplicates from a Sorted Singly Linked List

This script defines functions to build a singly linked list from input and eliminate all consecutive duplicate elements in the list. 
The script is designed to work with a list where elements are sorted in ascending order.

Functions:
    eliminate_duplicate(head): Remove consecutive duplicates from the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        """Initialize a new node with data and set the next node to None."""
        self.data = data
        self.next = None

def eliminate_duplicate(head):
    """
    Remove consecutive duplicates from the sorted singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.

    Returns:
    Node: The head of the modified linked list without consecutive duplicates.

    Example:
    - Given a linked list with head 'head', eliminate_duplicate(head) will remove all consecutive duplicates.
    """
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

def ll(arr):
    """
    Build a singly linked list from the given array.

    Parameters:
    - arr (list of int): The array containing the elements of the linked list.

    Returns:
    Node: The head node of the constructed linked list.
    """
    if not arr:
        return None

    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    """Print the elements of the linked list."""
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Example usage
arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])  # Excluding the last element (-1) which indicates the end of the list
l = eliminate_duplicate(l)
printll(l)
