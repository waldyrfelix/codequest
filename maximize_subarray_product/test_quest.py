from maximize_subarray_product.quest import maxSubarray


def test_maxSubarray_1():
    assert maxSubarray([-2, 3, -4, 1]) == 24


def test_maxSubarray_2():
    assert maxSubarray([1, 0, 1, 2]) == 2


def test_maxSubarray_3():
    assert maxSubarray([1]) == 1


def test_maxSubarray_4():
    input = [
        8,
        -1,
        6,
        -6,
        -6,
        6,
        -4,
        4,
        6,
        -7,
        9,
        -7,
        -3,
        3,
        9,
        -4,
        4,
        5,
        5,
        1,
        -6,
        -9,
        8,
        -8,
        -5,
        4,
        5,
        8,
        8,
        1,
        2,
        4,
        -2,
        -3,
        5,
        -4,
        -2,
        -4,
        -1,
        2,
        -3,
        2,
        -2,
        -9,
        3,
        -9,
        5,
        -1,
        2,
        -6,
    ]

    result = maxSubarray(input)
    assert result == 845344078334668264439808000000
