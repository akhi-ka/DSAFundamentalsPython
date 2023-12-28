# Understanding Recursion

## Introduction
This project explores recursion, a core concept in programming where a function calls itself to solve a problem. Recursion is effective for tasks that can be divided into similar, smaller subtasks, and is often simpler and more concise than iterative solutions.

## Core Concepts
- **Recursion:** A method calls itself with a slightly simpler version of the original problem.
- **Base Case:** The condition under which the recursion terminates to prevent infinite loops.
- **Recursion Step:** The process of making successive recursive calls.
- **Memory Usage:** Each recursive call creates a new copy of the method's variables in memory, which is cleared once the method returns a value.
- **Principle of Mathematical Induction (PMI):** Recursion is akin to PMI, as each step builds upon the previous one.

## Recursive Function Format
```python
def recursive_function(parameters):
    if test_for_base_case:
        return base_case_value
    elif test_for_another_base_case:
        return another_base_case_value
    else:
        # Perform some operations, then make a recursive call
        return recursive_function(modified_parameters)
```

## Setting Recursion Limits in Python
```python
import sys
sys.setrecursionlimit(3000)
```
