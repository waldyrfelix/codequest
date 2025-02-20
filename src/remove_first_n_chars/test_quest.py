from remove_first_n_chars.quest import removeFirstNChars


def test_removeFirstNChars_1():
    result = removeFirstNChars("hello", 2)
    assert result == "llo"


def test_removeFirstNChars_2():
    result = removeFirstNChars("programming", 4)
    assert result == "ramming"


def test_removeFirstNChars_3():
    result = removeFirstNChars("tree", 0)
    assert result == "tree"


def test_removeFirstNChars_4():
    result = removeFirstNChars("apple", 10)
    assert result == ""
