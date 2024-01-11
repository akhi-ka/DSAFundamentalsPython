"""
A Stack class implemented using two queues.

Attributes:
-----------
queue1: Queue
    The first queue used for implementing the stack.

queue2: Queue
    The second queue used for implementing the stack.

Methods:
--------
__init__(self):
    Initializes both the queue1 and queue2 data members.

push(self, element: T) -> None:
    Inserts an element of type T into the stack.
    Time complexity: O(1).

pop(self) -> T:
    Removes and returns the last element entered in the stack.

top(self) -> T:
    Returns the last element entered in the stack without removing it.

getSize(self) -> int:
    Returns the number of elements present in the stack.
    Time complexity: O(1).
"""
import queue


class StackUsingQueues:
    """
    Stack implementation using two queues.

    This class implements a stack data structure using two queues. It supports push, pop, top, and other standard stack operations.

    Attributes:
    - q1 (QueueUsingLL): The primary queue used for stack operations.
    - q2 (QueueUsingLL): The secondary queue used for assisting in stack operations.
    - curr_size (int): The number of elements in the stack.
    """

    def __init__(self):
        """
        Initialize the Stack with empty state.
        """
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.curr_size = 0

    def push(self, data):
        """
        Add an element to the top of the stack.

        Parameters:
        - data: The data to be added to the stack.

        Returns:
        None
        """
        self.curr_size += 1
        self.q2.enqueue(data)

        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.front())
            self.q1.dequeue()

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        Remove and return the top element from the stack.

        Returns:
        The data of the top element, or 0 if the stack is empty.
        """
        if self.q1.isEmpty():
            return 0
        self.curr_size -= 1
        return self.q1.dequeue()

    def top(self):
        """
        Return the top element of the stack without removing it.

        Returns:
        The data of the top element, or 0 if the stack is empty.
        """
        if self.q1.isEmpty():
            return 0
        return self.q1.front()

    def getSize(self):
        """
        Return the number of elements in the stack.

        Returns:
        The size of the stack.
        """
        return self.curr_size


# Example usage of the StackUsingQueues class
if __name__ == "__main__":
    s = StackUsingQueues()
    li = [int(ele) for ele in input().split()]
    i = 0
    while i < len(li):
        choice = li[i]
        if choice == -1:
            break
       
