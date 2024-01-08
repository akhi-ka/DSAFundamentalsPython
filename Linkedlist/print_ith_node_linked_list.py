"""
Python Script for Finding and Printing the ith Node in a Singly Linked List

This script defines functions to build a singly linked list from input and find and print the data of the node at a specific position ('i') in the list.
It demonstrates the use of iterative traversal in Python for linked lists and includes an example of how to use the functions.

Functions:
    ithNode(head, i): Find and return the node at the 'i-th' position in the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def ithNode(head, i):
    """
    Find and return the node at the 'i-th' position in the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.
    - i (int): The position of the node to find.

    Returns:
    Node: The node at the 'i-th' position, or None if the position is invalid.

    Example:
    - Given a linked list with head 'head' and a position 'i', ithNode(head, i) will return the node at the 'i-th' position.
    """
    count = 0
    current = head
    while current is not None and count < i:
        current = current.next
        count += 1
    return current

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
    i = int(input())
    l = ll(arr[:-1])  # Excluding the last element (-1) which indicates the end of the list
    node = ithNode(l, i)
    if node:
        print(node.data)
