"""
Problem
Given an array of integers nums and a non-negative integer targetDiff,
determine if there are two distinct elements in nums such that the absolute difference between them is targetDiff.

Return true if at least one such pair exists, otherwise return false.

Examples
hasSpecificDifference([8, 16, 15, 40], 8)
// returns true
// 16 - 8 = 8

hasSpecificDifference([1, 2, 3], 0)
// returns false
// There is no pair in the array that have a difference of 0.
"""

from typing import List


def hasSpecificDifference(nums: List[int], targetDiff: int) -> bool:
    for i, n in enumerate(nums):
        for j, m in enumerate(nums):
            if i != j and abs(n - m) == targetDiff:
                return True
    return False
