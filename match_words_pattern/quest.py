"""
Problem
Given a pattern string pattern and a string sentence, 
return true if sentence follows the same sequence as pattern. 
Each character in the pattern corresponds to a unique 
word in the sentence.

Examples
doesMatchPattern("xyx", "apple orange apple")
// returns true
// 'x' is 'apple' and 'y' is 'orange'.
 
doesMatchPattern("aba", "hello world world")
// returns false
// 'a' and 'b' don't consistently match.
 
doesMatchPattern("aaa", "banana banana banana")
// returns true
// 'a' always represents 'banana'.
"""


def doesMatchPattern(pattern: str, sentence: str) -> bool:
    pattern_list = list(pattern)
    sentence_list = sentence.split()

    if len(pattern_list) != len(sentence_list):
        return False

    matching = dict(zip(sentence_list, pattern_list))
    proof = [matching[s] for s in sentence_list]

    return "".join(proof) == pattern
