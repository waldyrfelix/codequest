from find_index.quest import myFindIndex


def test_myFindIndex_1():
    result = myFindIndex([1, 9, 5, 15], 5)
    assert result == 2


def test_myFindIndex_2():
    result = myFindIndex([1, 9, 5, 15], 15)
    assert result == 3


def test_myFindIndex_3():
    result = myFindIndex([1, 9, 5, 15], 4)
    assert result == -1
