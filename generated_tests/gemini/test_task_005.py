from solutions.task_005 import intersperse


def test_intersperse_empty_list():
    assert intersperse([], 4) == []


def test_intersperse_single_element():
    assert intersperse([1], 4) == [1]


def test_intersperse_docstring_example():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_intersperse_two_elements():
    assert intersperse([10, 20], 0) == [10, 0, 20]


def test_intersperse_negative_numbers():
    assert intersperse([-1, -2, -3], -99) == [-1, -99, -2, -99, -3]