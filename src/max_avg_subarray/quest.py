import math
from typing import List

"""
Problem
Given an array nums of integers and an integer k, find the maximum average
value of any contiguous subarray of size k and return its average rounded
down to the nearest integer.

Examples
maxAvgSubarray([1,12,-5,-6,50,3], 4)
// returns 12
// The subarray with the max avg is [12, -5, -6, 50]
// with an average score of 12.75, rounded down to 12

maxAvgSubarray([5], 1)
// returns 5
// There's only one subarray which is 5
"""


def maxAvgSubarray(nums: List[int], k: int) -> int:
    avgs: List[int] = []

    for i in range(len(nums) - k + 1):
        sub = nums[i : i + k]
        avg = sum(sub) / float(len(sub))
        avgs.append(avg)

    return math.floor(max(avgs))
