from max_len_asc_subsequence.quest import findMaxAscendingLength


def test_findMaxAscendingLength_1():
    assert findMaxAscendingLength([6, 5, -1, 3, 2, 4, 42, 9]) == 4


def test_findMaxAscendingLength_2():
    assert findMaxAscendingLength([5, 4, 3, 2, 1]) == 1


def test_findMaxAscendingLength_3():
    assert findMaxAscendingLength([-1, 0, 1, 2, 3]) == 5


def test_findMaxAscendingLength_4():
    assert findMaxAscendingLength([5, 6, 7, 8, 1, 2, 3, 4]) == 4
