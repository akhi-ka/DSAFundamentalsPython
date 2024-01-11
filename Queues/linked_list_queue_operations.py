"""
A Queue class implemented using a linked list.

Attributes:
-----------
None (All data members are private)

Methods:
--------
__init__(self):
    Initializes the data members of the Queue class.

enqueue(self, element: T) -> None:
    Inserts an element of type T into the queue.
    Time complexity: O(1).

dequeue(self) -> T:
    Removes and returns the first element entered in the queue.
    Time complexity: O(1).

front(self) -> T:
    Returns the first element entered in the queue without removing it.
    Time complexity: O(1).

size(self) -> int:
    Returns the number of elements present in the queue.
    Time complexity: O(1).

isEmpty(self) -> bool:
    Checks whether the queue is empty or not. Returns True if empty, False otherwise.
    Time complexity: O(1).
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
    The data of the front element, or 0 if the queue is empty.
    """
    if self.__head is None:
      return 0
    data = self.__head.data
    self.__head = self.__head.next
    self.__count -= 1
    return data

  def front(self):
    """
    Return the front element of the queue without removing it.

    Returns:
    The data of the front element, or 0 if the queue is empty.
    """
    if self.__head is None:
      return 0
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


# Example usage of the QueueUsingLL class
if __name__ == "__main__":
  q = QueueUsingLL()
  li = [int(ele) for ele in input().split()]
  i = 0
  while i < len(li):
    choice = li[i]
    if choice == -1:
      break
    elif choice == 1:
      q.enqueue(li[i + 1])
      i += 1
    elif choice == 2:
      ans = q.dequeue()
      print(ans if ans != 0 else -1)
    elif choice == 3:
      ans = q.front()
      print(ans if ans != 0 else -1)
    elif choice == 4:
      print(q.getSize())
    elif choice == 5:
      print('true' if q.isEmpty() else 'false')
    i += 1