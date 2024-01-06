"""
Python Script for Mirroring a Binary Tree

This script defines functions to build a binary tree from level order input and mirror the tree (i.e., swap the left and right children of all nodes).
It demonstrates the use of recursion in Python for tree manipulation and includes an example of how to use the functions.

Functions:
    mirrorBinaryTree(root): Mirror the binary tree.
    buildLevelTree(levelorder): Build a binary tree from level order input.
    printLevelATNewLine(root): Print the tree in level order, each level on a new line.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirrorBinaryTree(root):
    """
    Mirror the binary tree.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    None: The function mirrors the tree in place.

    Example:
    - Given a binary tree with root 'root', mirrorBinaryTree(root) will mirror the tree.
    """
    if root is None:
        return
    root.left, root.right = root.right, root.left
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)

def printLevelATNewLine(root):
    """
    Print the tree in level order, each level on a new line.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    None: The function prints the tree level by level.

    Example:
    - Given a binary tree with root 'root', printLevelATNewLine(root) will print the tree in level order.
    """
    if root is None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left is not None:
                outputQ.put(curr.left)
            if curr.right is not None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

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
    # Example usage of the functions
    levelOrder = [int(i) for i in input().strip().split()]
    root = buildLevelTree(levelOrder)
    mirrorBinaryTree(root)
    print("Mirrored tree level by level:")
    printLevelATNewLine(root)
