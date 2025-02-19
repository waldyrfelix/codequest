from valid_parentheses.quest import validParentheses


def test_valid_parentheses_1():
    assert validParentheses("{[()]}") == True


def test_valid_parentheses_2():
    assert validParentheses("{[(])}") == False


def test_valid_parentheses_3():
    assert validParentheses("({})[({})]") == True


def test_valid_parentheses_4():
    assert validParentheses("({})[({)}]") == False


def test_valid_parentheses_5():
    assert validParentheses("({[})") == False


def test_valid_parentheses_6():
    assert validParentheses("{[(") == False


def test_valid_parentheses_7():
    assert validParentheses("") == False


def test_valid_parentheses_8():
    assert validParentheses("]]") == False


def test_valid_parentheses_9():
    assert validParentheses("[((()))]") == True


def test_valid_parentheses_10():
    assert (
        validParentheses(
            "(((((()(()))(()((()((())))))(((()()((((()(((()))))))((()()))))))))))))"
        )
        == False
    )
