"""
Python Script for Finding the Diameter of a Binary Tree

This script defines functions to build a binary tree from level order input and calculate the diameter of the tree.
It demonstrates the use of recursion in Python for tree traversal and diameter calculation, and includes an example of how to use the functions.

Functions:
    diameter(root): Calculate the diameter of the binary tree.
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
    Calculate the height of a node in the binary tree.

    Parameters:
    - root (BinaryTreeNode): The node for which to calculate the height.

    Returns:
    int: The height of the tree from the node.
    """
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    """
    Calculate the diameter of the binary tree.

    The diameter is defined as the number of nodes on the longest path between two leaves in the tree.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    int: The diameter of the tree.

    Example:
    - Given a binary tree with root 'root', diameter(root) will return the diameter of the tree.
    """
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

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
    # Example usage of the diameter function
    levelOrder = [int(i) for i in input().strip().split()]
    root = buildLevelTree(levelOrder)
    print("Diameter of the binary tree:", diameter(root))
