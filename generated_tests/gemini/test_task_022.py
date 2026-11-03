from solutions.task_022 import filter_integers


def test_filter_integers_empty_list():
    assert filter_integers([]) == []


def test_filter_integers_docstring_examples():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]


def test_filter_integers_no_integers():
    assert filter_integers(['abc', 3.14, {}, [], None]) == []


def test_filter_integers_only_integers():
    assert filter_integers([10, -5, 0]) == [10, -5, 0]


def test_filter_integers_with_booleans():
    # In Python, bool is a subclass of int, so isinstance(True, int) is True
    assert filter_integers([True, False, 1, 2]) == [True, False, 1, 2]