"""

Problem
Given an array arr of integers, identify the length of the longest subsequence that increases strictly.

A subsequence is defined as a sequence that can be derived from the array 
by deleting some or no elements without changing the order of the remaining elements.

Examples
findMaxAscendingLength([6, 5, -1, 3, 2, 4, 42, 9])
// returns 4
// Longest ascending subsequence is [-1, 3, 4, 42]
// which is of length 4
 
findMaxAscendingLength([5, 4, 3, 2, 1])
// returns 1

"""

from typing import List


def findMaxAscendingLength(arr: List[int]) -> int:
    n = len(arr)

    if n == 0:
        return 0

    aux = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                aux[i] = max(aux[i], aux[j] + 1)

    return max(aux)
