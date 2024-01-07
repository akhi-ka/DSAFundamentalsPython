"""
Python Script for Printing a Binary Tree Level-wise

This script defines functions to build a binary tree from level order input and print the tree in a level-wise order.
It demonstrates the use of a queue in Python for level-wise traversal and includes an example of how to use the functions.

Functions:
    printLevelWise(root): Print the binary tree level-wise.
    buildLevelTree(levelorder): Build a binary tree from level order input.
"""

import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelWise(root):
    """
    Print the binary tree in level-wise order.

    For each node, prints the node's data and the data of its left and right children.

    Parameters:
    - root (BinaryTreeNode): The root node of the binary tree.

    Returns:
    None: The function prints the tree level by level.

    Example:
    - Given a binary tree with root 'root', printLevelWise(root) will print the tree in a level-wise order.
    """
    if root is None:
        return
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        curr = q.get()
        print(f"{curr.data}:", end='')
        if curr.left:
            print(f"L:{curr.left.data},", end='')
            q.put(curr.left)
        else:
            print("L:-1,", end='')

        if curr.right:
            print(f"R:{curr.right.data}", end='')
            q.put(curr.right)
        else:
            print("R:-1", end='')
        print()

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
    # Example usage of the printLevelWise function
    levelOrder = [int(i) for i in input().strip().split()]
    root = buildLevelTree(levelOrder)
    print("Binary tree printed level-wise:")
    printLevelWise(root)
