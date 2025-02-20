"""
Problem
Given a binary string s, return the number of non-empty substrings
that have the same number of 0's and 1's, and all the 0's and all
the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted
the number of times they occur.

Examples
countBinarySubstrings("11000110")
// returns 5
// Substrings: "1100", "0011", "10", "01", and "10".

countBinarySubstrings("100110")
// returns 4
// The harmonious designs are: "10", "0011", "10", and "01".
"""


def countBinarySubstrings(s: str) -> int:
    groups = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)

    subs = 0
    for i in range(1, len(groups)):
        subs += min(groups[i - 1], groups[i])

    return subs
