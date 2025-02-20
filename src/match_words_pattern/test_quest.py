from match_words_pattern.quest import doesMatchPattern


def test_match_pattern_1():
    assert doesMatchPattern("xyx", "apple orange apple") == True


def test_match_pattern_2():
    assert doesMatchPattern("aba", "hello world world") == False


def test_match_pattern_3():
    assert doesMatchPattern("aaa", "banana banana banana") == True


def test_match_pattern_4():
    assert doesMatchPattern("abcadeb", "I do what I have to do") == True


def test_match_pattern_5():
    assert doesMatchPattern("jjj", "ja ja ja ja") == False


def test_match_pattern_5():
    assert doesMatchPattern("abc", "ole ole ole") == False
