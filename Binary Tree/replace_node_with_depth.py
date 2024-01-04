"""
Python Script for Replacing Node Data with Depth in a Binary Tree

This script defines functions to build a binary tree from level order input and replace each node's data with the depth of the node.
It demonstrates the use of recursion in Python for tree manipulation and includes an example of how to use the functions.

Functions:
    replaceWithDepth(root, level=0): Replace each node's data with its depth in the binary tree.
    buildLevelTree(levelorder): Build a binary tree from level order input.
    inorder(root): Perform an inorder traversal of the binary tree.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def replaceWithDepth(root, level=0):
    """
    Replace each node's data with its depth in the binary tree.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.
    - level (int): The depth level of the node (default is 0 for the root).

    Returns:
    None: The function modifies the tree in place.

    Example:
    - Given a binary tree with root 'root', replaceWithDepth(root) will replace each node's data with its depth.
    """
    if root is None:
        return
    root.data = level
    replaceWithDepth(root.left, level + 1)
    replaceWithDepth(root.right, level + 1)

def inorder(root):
    """
    Perform an inorder traversal of the binary tree.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    None: The function prints the nodes in inorder traversal.

    Example:
    - Given a binary tree with root 'root', inorder(root) will print the nodes in inorder.
    """
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

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
    replaceWithDepth(root)
    print("Inorder traversal of modified tree:")
    inorder(root)
