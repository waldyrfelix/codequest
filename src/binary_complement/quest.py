"""
Problem
Given a positive integer num, compute its binary complement.
The binary complement is formed by flipping
all bits of its binary representation
(changing 0 to 1 and vice versa).

Return the decimal value of the binary complement.

Examples
findComplement(8)
// returns 7
// The binary representation of 8 is 1000
// its complement is 0111, which is 7 in decimal

findComplement(10)
// returns 5
// The binary representation of 10 is 1010
// its complement is 0101, which is 5 in decimal

findComplement(7)
// returns 0
// The binary representation of 7 is 111
// its complement is 000, which is 0 in decimal
"""


def findComplement(num: int) -> int:
    for mask in range(num):
        exp = 2**mask
        if exp >= num:
            return ~num & (exp - 1)
