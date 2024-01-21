# Dynamic Programming

## Introduction
This project delves into Dynamic Programming (DP), a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful for optimization problems where the solution can be constructed from solutions of its subproblems. Dynamic Programming is both a mathematical optimization method and a computer programming method.

## Core Concepts
- **Optimal Substructure:** A problem exhibits optimal substructure if an optimal solution can be constructed efficiently from optimal solutions of its subproblems.
- **Overlapping Subproblems:** A problem has overlapping subproblems if the same subproblems are solved multiple times.
- **Memoization:** Storing the results of expensive function calls and returning the cached result when the same inputs occur again.
- **Bottom-Up Approach:** Solving smaller subproblems first and using their solutions to construct solutions to bigger subproblems.
- **Top-Down Approach:** Breaking down the problem into subproblems, solving them as needed, and storing their solutions.

## Implementing Dynamic Programming in Python
```python
def fibonacci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

## Common Problems Solved Using Dynamic Programming
- Fibonacci Sequence
- Shortest Path Problems
- Knapsack Problem
- Coin Change Problem
- Longest Common Subsequence

## Challenges and Exercises
- Implement a dynamic programming solution for the Rod Cutting Problem.
- Write a program to find the minimum number of coins that make a given value.
- Develop a dynamic programming approach to solve the Longest Increasing Subsequence problem.