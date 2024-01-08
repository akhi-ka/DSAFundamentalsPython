"""
Python Script for Finding the Length of a Singly Linked List

This script defines functions to build a singly linked list from input and calculate its length using an iterative method.
It demonstrates the use of iterative traversal in Python for linked lists and includes an example of how to use the functions.

Functions:
    findlength(head): Calculate the length of the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findlength(head):
    """
    Calculate the length of the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.

    Returns:
    int: The length of the linked list.

    Example:
    - Given a linked list with head 'head', findlength(head) will return the length of the list.
    """
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count

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

if __name__ == "__main__":
    arr = list(int(i) for i in input().strip().split(' '))
    l = ll(arr[:-1])  # Excluding the last element (-1) which indicates the end of the list
    length = findlength(l)
    print(length)
