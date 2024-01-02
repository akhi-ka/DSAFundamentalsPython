"""
Python Script for Sum of All Nodes in a Binary Tree

This script defines functions to build a binary tree from level order input and calculate the sum of all nodes in the tree.
It demonstrates the use of recursion in Python for tree traversal and includes an example of how to use the functions.

Functions:
    sumOfAllNodes(root): Calculate the sum of all nodes in the binary tree.
    buildLevelTree(levelorder): Build a binary tree from level order input.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumOfAllNodes(root):
    """
    Calculate the sum of all nodes in the binary tree.

    The function recursively traverses the binary tree and sums up the value of each node.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    int: The sum of all nodes in the tree.

    Example:
    - Given a binary tree with root 'root', sumOfAllNodes(root) will return the sum of all nodes in the tree.
    """
    if root is None:
        return 0
    return root.data + sumOfAllNodes(root.left) + sumOfAllNodes(root.right)

def buildLevelTree(levelorder):
    """
    Build a binary tree from level order input.

    Parameters:
    - levelorder (list of int): Level order traversal of the tree, where '-1' indicates the absence of a child.

    Returns:
    BinaryTreeNode: The root node of the constructed binary tree.
    """
    if len(levelorder) == 0 or levelorder[0] == -1:
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
    # Example usage of the functions
    levelOrder = [5, 6, 10, 2, 3, -1, -1, -1, -1, -1, 9, -1, -1]
    root = buildLevelTree(levelOrder)
    print(f"Sum of all nodes in the binary tree: {sumOfAllNodes(root)}")

    # Additional Example
    levelOrder = [1, 2, 3, 4, 5, -1, -1]
    root = buildLevelTree(levelOrder)
    print(f"Sum of all nodes in the binary tree: {sumOfAllNodes(root)}")
