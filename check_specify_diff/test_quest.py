from check_specify_diff.quest import hasSpecificDifference


def test_hasSpecificDifference_1():
    result = hasSpecificDifference([8, 16, 15, 40], 8)

    assert result == True


def test_hasSpecificDifference_2():
    result = hasSpecificDifference([1, 2, 3], 0)

    assert result == False


def test_hasSpecificDifference_3():
    result = hasSpecificDifference([10, 100, 1000, 10000], 990)

    assert result == True


def test_hasSpecificDifference_4():
    result = hasSpecificDifference([0, 0, 0, 0], 0)

    assert result == True
