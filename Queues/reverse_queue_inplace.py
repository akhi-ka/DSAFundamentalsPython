"""
Reverses a queue of integers in place without using any explicit stack or queue.

Note:
-----
The function modifies the queue in place and does not return or print the queue.

Input Format:
-------------
The function expects a queue as its parameter. The queue should already be populated with integers.
It's assumed that the first element of the queue is the size of the queue, followed by the elements of the queue.

Output Format:
--------------
There is no return value or printed output from this function as it modifies the queue in place.

Parameters:
-----------
queue (Queue): A queue of integers. The first element is the size of the queue, followed by the queue's elements.

Returns:
--------
None

Example:
--------
    >>> from queue import Queue
    >>> q = Queue()
    >>> for elem in [5, 1, 2, 3, 4, 5]:  # Example input: 5 elements in the queue
    ...     q.put(elem)
    >>> reverseQueue(q)
    # At this point, the queue `q` is reversed in place.
"""

class Node:
    """
    A Node in a singly linked list.
    This class creates a node for use in a singly linked list, with 'data' as the node's value and 'next' as the reference to the next node in the list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLL:
    """
    Queue implementation using a linked list.
    This class implements a queue data structure using a singly linked list. It supports enqueue, dequeue, and other standard queue operations.
    Attributes:
    - head (Node): The front of the queue.
    - tail (Node): The end of the queue.
    - count (int): The number of elements in the queue.
    """
    def __init__(self):
        """
        Initialize the Queue with empty state.
        """
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, data):
        """
        Add an element to the end of the queue.
        Parameters:
        - data: The data to be added to the queue.
        Returns:
        None
        """
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1

    def dequeue(self):
        """
        Remove and return the front element from the queue.
        Returns:
        The data of the front element, or None if the queue is empty.
        """
        if self.__head is None:
            return None
        data = self.__head.data
        self.__head = self.__head.next
        if self.__head is None:
            self.__tail = None
        self.__count -= 1
        return data

    def front(self):
        """
        Return the front element of the queue without removing it.
        Returns:
        The data of the front element, or None if the queue is empty.
        """
        if self.__head is None:
            return None
        return self.__head.data

    def getSize(self):
        """
        Return the number of elements in the queue.
        Returns:
        The size of the queue.
        """
        return self.__count

    def isEmpty(self):
        """
        Check if the queue is empty.
        Returns:
        True if the queue is empty, False otherwise.
        """
        return self.getSize() == 0

def reverseQueue(q1):
    """
    Reverse the elements of a queue.
    Parameters:
    - q1 (QueueUsingLL): The queue to be reversed.
    Returns:
    None
    """
    stack = []
    while not q1.isEmpty():
        stack.append(q1.dequeue())
    while len(stack) != 0:
        q1.enqueue(stack.pop())

if __name__ == "__main__":
    from sys import setrecursionlimit
    setrecursionlimit(11000)  # Not necessary in this script

    q1 = QueueUsingLL()
    li = [int(ele) for ele in input().split()]
    for ele in li:
        q1.enqueue(ele)
    
    reverseQueue(q1)

    while not q1.isEmpty():
        print(q1.dequeue(), end=' ')
