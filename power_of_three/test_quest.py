from power_of_three.quest import isPowerOfThree


def test_isPowerOfThree_1():
    result = isPowerOfThree(81)
    assert result == True


def test_isPowerOfThree_2():
    result = isPowerOfThree(9)

    assert result == True


def test_isPowerOfThree_3():
    result = isPowerOfThree(2)
    assert result == False


def test_isPowerOfThree_4():
    result = isPowerOfThree(26)
    assert result == False


def test_isPowerOfThree_5():
    result = isPowerOfThree(3)
    assert result == True


def test_isPowerOfThree_6():
    result = isPowerOfThree(1)
    assert result == True
