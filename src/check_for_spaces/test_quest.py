from check_for_spaces.quest import stringContainsSpace


def test_stringContainsSpace_1():
    result = stringContainsSpace("Hello world")
    assert result == True


def test_stringContainsSpace_2():
    result = stringContainsSpace("NoSpacesHere")
    assert result == False


def test_stringContainsSpace_3():
    result = stringContainsSpace("  Leading spaces")
    assert result == True


def test_stringContainsSpace_4():
    result = stringContainsSpace("Trailing spaces  ")
    assert result == True
