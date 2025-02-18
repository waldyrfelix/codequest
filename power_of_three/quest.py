"""
Problem
Given a positive integer num, return true if num is a power of three, and false otherwise.

Examples
isPowerOfThree(81) 
// returns true
// 81 is a power of three (3^4)
 
isPowerOfThree(9) 
// returns true
// 9 is a power of three (3^2)
 
isPowerOfThree(2) 
// returns false
// 2 is not a power of three
"""


def isPowerOfThree(num: int) -> bool:
    for pow in range(num):
        result = 3**pow
        if result >= num:
            return result == num

    return False
