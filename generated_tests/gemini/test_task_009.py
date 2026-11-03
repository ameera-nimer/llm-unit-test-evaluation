from solutions.task_009 import rolling_max


def test_rolling_max_empty_list():
    assert rolling_max([]) == []


def test_rolling_max_single_element():
    assert rolling_max([5]) == [5]


def test_rolling_max_docstring_example():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]


def test_rolling_max_strictly_increasing():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_rolling_max_strictly_decreasing():
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]


def test_rolling_max_negative_numbers():
    assert rolling_max([-5, -2, -8, -1]) == [-5, -2, -2, -1]