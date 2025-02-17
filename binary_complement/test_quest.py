from binary_complement.quest import findComplement


def test_findComplement_1():
    result = findComplement(8)
    assert result == 7


def test_findComplement_2():
    result = findComplement(10)
    assert result == 5


def test_findComplement_3():
    result = findComplement(7)
    assert result == 0
