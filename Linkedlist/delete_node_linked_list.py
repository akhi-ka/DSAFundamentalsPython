"""
Python Script for Deleting a Node from a Singly Linked List

This script defines functions to build a singly linked list from input and delete a node from a specific position in the list.
It demonstrates the use of recursion in Python for linked list manipulation and includes an example of how to use the functions.

Functions:
    deleteRec(head, i): Delete the node at the 'i-th' position in the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteRec(head, i):
    """
    Delete the node at the 'i-th' position in the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.
    - i (int): The position of the node to be deleted.

    Returns:
    Node: The head of the modified linked list.

    Example:
    - Given a linked list with head 'head' and a position 'i', deleteRec(head, i) will delete the node at the 'i-th' position.
    """
    if i < 0:
        return head
    if head is None:
        return None
    if i == 0:
        return head.next
    head.next = deleteRec(head.next, i - 1)
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

if __name__ == "__main__":
    arr = list(int(i) for i in input().strip().split(' '))
    i = int(input())
    l = ll(arr[:-1])  # Excluding the last element (-1) which indicates the end of the list
    l = deleteRec(l, i)
    # Printing the modified linked list
    current = l
    while current:
        print(current.data, end=' ')
        current = current.next
    print()
