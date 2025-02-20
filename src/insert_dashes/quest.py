"""
Problem
Given a string s and an array of integers indices, insert dashes ('-') at the specified indices in the string and return the modified string. The indices array will not contain duplicate values.

Examples
insertDashes("HelloWorld", [5])
// returns "Hello-World"

insertDashes("AddDashesHere", [3, 9])
// returns "Add-Dashes-Here"

"""

from typing import List


def insertDashes(s: str, indices: List[int]) -> str:
    word_list = list(s)
    index_list = list(set(indices))
    index_list.sort()

    for i, idx in enumerate(index_list):
        word_list.insert(i + idx, "-")

    return "".join(word_list)
