"""
Python Script for Checking if a Singly Linked List is a Palindrome

This script defines a function to check whether a given singly linked list is a palindrome. 
It uses the concept of reversing half of the list and then comparing it with the other half for palindrome checking.

Functions:
    is_palindrome(llist): Check if the given singly linked list is a palindrome.
"""

class Node:
    def __init__(self, data):
        """Initialize a new node with data and set the next node to None."""
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize an empty linked list with head and last node as None."""
        self.head = None
        self.last_node = None

    def append(self, data):
        """Append a new node with the given data to the end of the linked list."""
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def get_prev_node(self, ref_node):
        """Get the node previous to the given reference node in the linked list."""
        current = self.head
        while current and current.next != ref_node:
            current = current.next
        return current

def is_palindrome(llist):
    """
    Check if the linked list is a palindrome.

    This function compares the data of nodes from the start and end of the linked list
    and moves towards the center to determine if it is a palindrome.

    Parameters:
    - llist (LinkedList): The linked list to be checked.

    Returns:
    bool: True if the linked list is a palindrome, False otherwise.

    Example:
    - Given a linked list 'llist', is_palindrome(llist) returns True if the list is a palindrome.
    """
    start = llist.head
    end = llist.last_node
    while start != end and end.next != start:
        if start.data != end.data:
            return False
        start = start.next
        end = llist.get_prev_node(end)
    return True

if __name__ == "__main__":
    # Example usage of the is_palindrome function
    a_llist = LinkedList()
    data_list = input("Enter the elements of the linked list: ").split()
    for data in data_list:
        if int(data) != -1:
            a_llist.append(int(data))

    if is_palindrome(a_llist):
        print('true')
    else:
        print('false')
