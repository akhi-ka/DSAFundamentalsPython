"""
Python Script for Tower of Hanoi Puzzle

This script defines a function `towerOfHanoi` to solve the Tower of Hanoi puzzle, a classic problem in recursion.
It demonstrates the use of recursion in Python for solving this puzzle and includes an example of how to use the function.

Functions:
    towerOfHanoi(n, a, b, c): Solve the Tower of Hanoi puzzle for 'n' disks.
"""

def towerOfHanoi(n, a, b, c):
    """
    Solve the Tower of Hanoi puzzle for 'n' disks.

    The function moves 'n' disks from rod 'a' (source) to rod 'c' (destination) using rod 'b' (helper),
    following the rules of the Tower of Hanoi puzzle.

    Parameters:
    - n (int): The number of disks.
    - a (str): The name of the source rod.
    - b (str): The name of the helper rod.
    - c (str): The name of the destination rod.

    Returns:
    None: The function prints the steps to solve the puzzle.

    Example:
    - towerOfHanoi(3, 'source', 'helper', 'destination') prints the steps to solve the puzzle for 3 disks.
    """
    if n == 1:
        print(f"Move 1st disk from {a} to {c}")
        return
    towerOfHanoi(n - 1, a, c, b)
    print(f"Move {n}th disk from {a} to {c}")
    towerOfHanoi(n - 1, b, a, c)

if __name__ == "__main__":
    # Example usage of the towerOfHanoi function
    n_disks = 3
    print(f"Solving Tower of Hanoi for {n_disks} disks:")
    towerOfHanoi(n_disks, "source", "helper", "destination")

    # Additional Example
    n_disks = 4
    print(f"\nSolving Tower of Hanoi for {n_disks} disks:")
    towerOfHanoi(n_disks, "source", "helper", "destination")
