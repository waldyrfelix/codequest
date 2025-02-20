"""
Problem
Given an integer array nums, implement a function to find the subarray that yields the largest product and return this maximum product.

Examples
maxSubarray([-2, 3, -4, 1])
// return 24
// Why? Largest subarray is [-2, 3, -4] which is 24

"""

import math
from typing import List


def maxSubarray(nums: List[int]) -> int:
    count = len(nums)
    max_prod = 0
    for i in range(count):
        for j in range(i + 1, count + 1):
            subarray_prod = math.prod(nums[i:j])
            if subarray_prod > max_prod:
                max_prod = subarray_prod
                print(max_prod)

    return max_prod
