from solutions.task_014 import all_prefixes


def test_all_prefixes_empty_string():
    assert all_prefixes('') == []


def test_all_prefixes_single_character():
    assert all_prefixes('a') == ['a']


def test_all_prefixes_docstring_example():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']


def test_all_prefixes_longer_string():
    assert all_prefixes('python') == ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']


def test_all_prefixes_with_spaces():
    assert all_prefixes('a b') == ['a', 'a ', 'a b']