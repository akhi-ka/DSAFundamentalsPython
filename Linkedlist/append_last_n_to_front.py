"""
Python Script for Appending Last 'N' Nodes to Front in a Singly Linked List

This script defines functions to build a singly linked list from input and append the last 'N' nodes to the front of the list.
It demonstrates the use of iterative list manipulation in Python for linked lists and includes an example of how to use the functions.

Functions:
    append_LinkedList(head, n): Append the last 'n' nodes to the front of the linked list.
    ll(arr): Build a singly linked list from input.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    """
    Calculate the length of the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.

    Returns:
    int: The length of the linked list.
    """
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def append_LinkedList(head, n):
    """
    Append the last 'n' nodes to the front of the singly linked list.

    Parameters:
    - head (Node): The head node of the linked list.
    - n (int): The number of nodes to move from the end to the front.

    Returns:
    Node: The new head of the modified linked list.

    Example:
    - Given a linked list with head 'head' and a number 'n', append_LinkedList(head, n) rearranges the list and returns the new head.
    """
    if not head or not head.next or n <= 0:
        return head

    l = length(head)
    if n >= l:
        return head

    count = 0
    current = head
    while count < l - n - 1:
        current = current.next
        count += 1
    
    new_head = current.next
    current.next = None
    temp = new_head
    while temp.next:
        temp = temp.next
    temp.next = head

    return new_head

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
    n = int(input())
    l = ll(arr[:-1])  # Excluding the last element (-1) which indicates
