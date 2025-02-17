from max_avg_subarray.quest import maxAvgSubarray


def test_maxAvgSubarray_1():
    result = maxAvgSubarray([1, 12, -5, -6, 50, 3], 4)
    assert result == 12


def test_maxAvgSubarray_2():
    result = maxAvgSubarray([5], 1)
    assert result == 5


def test_maxAvgSubarray_3():
    result = maxAvgSubarray([1, 2, 3, 4, 5, 6], 3)
    assert result == 5
