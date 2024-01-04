"""
Python Script for Counting Nodes Greater Than X in a Binary Tree

This script defines functions to build a binary tree from level order input and count the number of nodes in the tree that have values greater than a specified integer X.
It demonstrates the use of recursion in Python for tree traversal and counting, and includes an example of how to use the functions.

Functions:
    countNodesGreaterThanX(root, x): Count nodes in the binary tree with values greater than x.
    buildLevelTree(levelorder): Build a binary tree from level order input.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countNodesGreaterThanX(root, x):
    """
    Count the number of nodes in the binary tree that have values greater than x.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.
    - x (int): The value to compare each node's data with.

    Returns:
    int: The count of nodes with values greater than x.

    Example:
    - Given a binary tree with root 'root' and an integer x, countNodesGreaterThanX(root, x) will return the count of nodes whose values are greater than x.
    """
    if root is None:
        return 0
    count = 1 if root.data > x else 0
    count += countNodesGreaterThanX(root.left, x)
    count += countNodesGreaterThanX(root.right, x)
    return count

def buildLevelTree(levelorder):
    """
    Build a binary tree from level order input.

    Parameters:
    - levelorder (list of int): Level order traversal of the tree, where '-1' indicates the absence of a child.

    Returns:
    BinaryTreeNode: The root node of the constructed binary tree.
    """
    if len(levelorder) <= 0 or levelorder[0] == -1:
        return None

    root = BinaryTreeNode(levelorder[0])
    q = queue.Queue()
    q.put(root)
    i = 1
    while not q.empty() and i < len(levelorder):
        currentNode = q.get()
        leftChild = levelorder[i]
        i += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        if i < len(levelorder):
            rightChild = levelorder[i]
            i += 1
            if rightChild != -1:
                rightNode = BinaryTreeNode(rightChild)
                currentNode.right = rightNode
                q.put(rightNode)
    return root

if __name__ == "__main__":
    # Example usage of the countNodesGreaterThanX function
    levelOrder = [8, 3, 10, 1, 6, -1, 14, -1, -1, 4, 7, 13, -1, -1, -1, -1, -1, -1, -1]
    x = 8
    root = buildLevelTree(levelOrder)
    print(f"Number of nodes greater than {x}: {countNodesGreaterThanX(root, x)}")

    # Additional Example
    levelOrder = [1, 2, 3, 4, 5, -1, -1]
    x = 3
    root = buildLevelTree(levelOrder)
    print(f"Number of nodes greater than {x}: {countNodesGreaterThanX(root, x)}")
