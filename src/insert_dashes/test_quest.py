from insert_dashes.quest import insertDashes


def test_insert_dashes_1():
    r = insertDashes("HelloWorld", [5])
    assert r == "Hello-World"


def test_insert_dashes_2():
    r = insertDashes("AddDashesHere", [3, 9])
    assert r == "Add-Dashes-Here"


def test_insert_dashes_3():
    r = insertDashes("HiMyFriend", [2, 2, 4])
    assert r == "Hi-My-Friend"
