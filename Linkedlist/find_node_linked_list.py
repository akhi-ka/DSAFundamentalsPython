"""
Python Script for Finding a Node in a Singly Linked List

This script defines functions to build a singly linked list from input and find the index of a specified number in the list.
It demonstrates the use of recursion in Python for linked list manipulation and includes an example of how to use the functions.

Functions:
    findNode(head, number, index): Find and return the index of the specified number in the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findNode(head, number, index):
    """
    Find and return the index of the specified number in the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.
    - number (int): The number to find in the linked list.
    - index (int): The starting index for the search, initially set to 0.

    Returns:
    int: The index of the number if found, -1 otherwise.

    Example:
    - Given a linked list with head 'head' and a number 'number', findNode(head, number, 0) will return the index of the number.
    """
    if head is None:
        return -1
    if head.data == number:
        return index
    return findNode(head.next, number, index + 1)

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
    numberToFind = int(input())
    index = findNode(l, numberToFind, 0)
    print(index)
