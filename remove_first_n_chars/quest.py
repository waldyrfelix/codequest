from typing import List

"""
Problem
Given a string word and an integer n, return a new string with the first n characters removed from word. 
If n is greater than the length of word, return an empty string.

Examples
removeFirstNChars('hello', 2)
// 'llo'
 
removeFirstNChars('programming', 4)
// 'ramming'
 
removeFirstNChars('tree', 0)
// 'tree'
 
removeFirstNChars('apple', 10)
// ''
"""


def removeFirstNChars(word: str, n: int) -> str:
    if n >= len(word):
        return ""

    return word[n:]
