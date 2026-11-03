from solutions.task_012 import longest


def test_longest_empty_list():
    assert longest([]) is None


def test_longest_same_length_returns_first():
    assert longest(['a', 'b', 'c']) == 'a'


def test_longest_docstring_example():
    assert longest(['a', 'bb', 'ccc']) == 'ccc'


def test_longest_single_string():
    assert longest(['hello']) == 'hello'


def test_longest_multiple_same_length_mix():
    assert longest(['short', 'longer', 'longest', 'lengthy']) == 'longest'


def test_longest_with_empty_strings():
    assert longest(['', 'a', 'ab']) == 'ab'