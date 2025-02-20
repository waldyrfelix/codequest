"""
Problem
Given a string text, return true if the string contains at least one space, and false otherwise.

Examples
stringContainsSpace('Hello world') // true
stringContainsSpace('NoSpacesHere') // false
stringContainsSpace('  Leading spaces') // true
stringContainsSpace('Trailing spaces  ') // true
"""


def stringContainsSpace(text: str) -> bool:
    return " " in text
