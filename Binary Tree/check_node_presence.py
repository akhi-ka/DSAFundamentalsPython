"""
Python Script for Checking if a Node is Present in a Binary Tree

This script defines functions to build a binary tree from level order input and check if a node with a given data value is present in the tree.
It demonstrates the use of recursion in Python for tree traversal and node searching, and includes an example of how to use the functions.

Functions:
    isNodePresent(root, x): Check if a node with data 'x' is present in the binary tree.
    buildLevelTree(levelorder): Build a binary tree from level order input.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isNodePresent(root, x):
    """
    Check if a node with data 'x' is present in the binary tree.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.
    - x (int): The data value to search for in the tree.

    Returns:
    bool: True if a node with data 'x' is found, False otherwise.

    Example:
    - Given a binary tree with root 'root' and an integer 'x', isNodePresent(root, x) will return True if a node with data 'x' is present, otherwise False.
    """
    if root is None:
        return False
    if root.data == x:
        return True
    leftSearch = isNodePresent(root.left, x)
    rightSearch = isNodePresent(root.right, x)
    return leftSearch or rightSearch

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
    # Example usage of the isNodePresent function
    levelOrder = [int(i) for i in input().strip().split()]
    root = buildLevelTree(levelOrder)
    x = int(input())
    found = isNodePresent(root, x)
    print('true' if found else 'false')
