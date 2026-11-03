from solutions.task_023 import strlen


def test_strlen_empty_string():
    assert strlen('') == 0


def test_strlen_docstring_example():
    assert strlen('abc') == 3


def test_strlen_single_character():
    assert strlen('a') == 1


def test_strlen_special_characters():
    assert strlen('!@#$%^&*()') == 10


def test_strlen_with_spaces():
    assert strlen('hello world') == 11