"""
Python Script for Pre-order Traversal of a Binary Tree

This script defines functions to build a binary tree from level order input and perform a pre-order traversal of the tree.
It demonstrates the use of recursion in Python for tree traversal and includes an example of how to use the functions.

Functions:
    preOrder(root): Perform a pre-order traversal of the binary tree.
    buildLevelTree(levelorder): Build a binary tree from level order input.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    """
    Perform a pre-order traversal of the binary tree.

    The function visits each node in the pre-order sequence: root, left subtree, right subtree.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    None: The function prints the nodes in pre-order traversal.

    Example:
    - Given a binary tree with root 'root', preOrder(root) will print the nodes in pre-order.
    """
    if root:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)

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
    # Example usage of the preOrder function
    levelOrder = [8, 3, 10, 1, 6, -1, 14, -1, -1, 4, 7, 13, -1, -1, -1, -1, -1, -1, -1]
    root = buildLevelTree(levelOrder)
    print("Pre-order traversal of the binary tree:")
    preOrder(root)

    # Additional Example
    levelOrder = [1, 2, 3, 4, 5, -1, -1]
    root = buildLevelTree(levelOrder)
    print("\nPre-order traversal of another binary tree:")
    preOrder(root)
