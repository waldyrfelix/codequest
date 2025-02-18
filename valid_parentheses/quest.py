"""
Problem
Given a string s containing just the characters '(', ')', ', ', '[' and ']', 
determine if the input string is valid. An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Examples
validParentheses("{[()]}")
// true
 
validParentheses("{[(])}")
// false
validParentheses("({})[({})]")
// true
validParentheses("({})[({)}]")
// false
validParentheses("({[})")
// false
"""

pairs = {"{": "}", "(": ")", "[": "]"}


def match_pair(s: str, i: int) -> bool:
    n = len(s)
    token = s[i]

    if i == n - 1:
        return True

    if token in pairs:
        return match_pair(s, i + 1)

    prev_token = s[i - 1]
    return token == pairs[prev_token]


def validParentheses(s: str) -> bool:
    if len(s) == 0:
        return False

    if len(s) % 2 > 0:
        return False

    if s[0] not in pairs:
        return False

    if not all([s.count(p) == s.count(pairs[p]) for p in pairs]):
        return False

    return all([match_pair(s, i) for i, v in enumerate(s) if v in pairs])
