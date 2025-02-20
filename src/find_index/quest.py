from typing import List

"""
Problem
Given an array of integers numbers and an integer target, return the index of target in numbers.
If target is not present in the array, return -1.

Examples:
myFindIndex([1, 9, 5, 15], 5)
// 2
// numbers[2] = 5, so the target indice is 2.

myFindIndex([1, 9, 5, 15], 15) // 3
myFindIndex([1, 9, 5, 15], 4) // -1
"""


def myFindIndex(numbers: List[int], target: int) -> int:
    try:
        return numbers.index(target)
    except ValueError:
        return -1
