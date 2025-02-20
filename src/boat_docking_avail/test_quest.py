from boat_docking_avail.quest import canDockBoats


def test_canDockBoats_1():
    r = canDockBoats([0, 1, 0, 0, 0, 1, 0], 1)
    assert r == True


def test_canDockBoats_2():
    r = canDockBoats([1, 0, 0, 0, 1, 0, 0], 2)
    assert r == True


def test_canDockBoats_3():
    r = canDockBoats([1, 0, 1, 0, 1, 0, 1], 1)
    assert r == False
