"""
Python Script for Finding the Height of a Binary Tree

This script defines functions to build a binary tree from level order input and find the height of the tree.
It demonstrates the use of recursion in Python for tree traversal and height calculation, and includes an example of how to use the functions.

Functions:
    height(root): Calculate the height of the binary tree.
    buildLevelTree(levelorder): Build a binary tree from level order input.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    """
    Calculate the height of the binary tree.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    int: The height of the tree.

    Example:
    - Given a binary tree with root 'root', height(root) will return the height of the tree.
    """
    if root is None:
        return 0
    lDepth = height(root.left)
    rDepth = height(root.right)
    return max(lDepth, rDepth) + 1

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
    # Example usage of the height function
    levelOrder = [10, 9, 4, -1, -1, 5, 8, -1, 6, -1, -1, 3, -1, -1, -1]
    root = buildLevelTree(levelOrder)
    print(f"Height of the binary tree: {height(root)}")

    # Additional Example
    levelOrder = [1, 2, 3, 4, 5, -1, -1]
    root = buildLevelTree(levelOrder)
    print(f"Height of another binary tree: {height(root)}")
