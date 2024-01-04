"""
Python Script for Post-order Traversal of a Binary Tree

This script defines functions to build a binary tree from level order input and perform a post-order traversal of the tree.
It demonstrates the use of recursion in Python for tree traversal and includes an example of how to use the functions.

Functions:
    postOrder(root): Perform a post-order traversal of the binary tree.
    buildLevelTree(levelorder): Build a binary tree from level order input.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postOrder(root):
    """
    Perform a post-order traversal of the binary tree.

    The function visits each node in the post-order sequence: left subtree, right subtree, root.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    None: The function prints the nodes in post-order traversal.

    Example:
    - Given a binary tree with root 'root', postOrder(root) will print the nodes in post-order.
    """
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')

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
    # Example usage of the postOrder function
    levelOrder = [8, 3, 10, 1, 6, -1, 14, -1, -1, 4, 7, 13, -1, -1, -1, -1, -1, -1, -1]
    root = buildLevelTree(levelOrder)
    print("Post-order traversal of the binary tree:")
    postOrder(root)

    # Additional Example
    levelOrder = [1, 2, 3, 4, 5, -1, -1]
    root = buildLevelTree(levelOrder)
    print("\nPost-order traversal of another binary tree:")
    postOrder(root)
