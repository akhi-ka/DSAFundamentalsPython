"""
Python Script for Finding Nodes Without Sibling in a Binary Tree

This script defines functions to build a binary tree from level order input and find nodes that do not have a sibling.
It demonstrates the use of recursion in Python for tree traversal and includes an example of how to use the functions.

Functions:
    nodesWithoutSibling(root): Find and print nodes that do not have a sibling in the binary tree.
    buildLevelTree(levelorder): Build a binary tree from level order input.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesWithoutSibling(root):
    """
    Find and print nodes in the binary tree that do not have a sibling.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    None: The function prints the nodes without siblings.

    Example:
    - Given a binary tree with root 'root', nodesWithoutSibling(root) will print the nodes that do not have siblings.
    """
    if root is None:
        return
    if root.left is not None and root.right is None:
        print(root.left.data)
        nodesWithoutSibling(root.left)
    elif root.right is not None and root.left is None:
        print(root.right.data)
        nodesWithoutSibling(root.right)
    else:
        nodesWithoutSibling(root.left)
        nodesWithoutSibling(root.right)

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
    # Example usage of the nodesWithoutSibling function
    levelOrder = [int(i) for i in input().strip().split()]
    root = buildLevelTree(levelOrder)
    print("Nodes without sibling:")
    nodesWithoutSibling(root)
