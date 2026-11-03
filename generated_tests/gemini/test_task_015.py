from solutions.task_015 import string_sequence


def test_string_sequence_zero():
    assert string_sequence(0) == '0'


def test_string_sequence_docstring_example():
    assert string_sequence(5) == '0 1 2 3 4 5'


def test_string_sequence_one():
    assert string_sequence(1) == '0 1'


def test_string_sequence_larger_number():
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'


def test_string_sequence_negative_number():
    # Since range(0 + 1) or range(n+1) for negative n returns empty, range(-1 + 1) -> range(0) -> ''
    # Let's see what string_sequence(-1) returns: range(0) -> [] -> ''
    assert string_sequence(-1) == ''