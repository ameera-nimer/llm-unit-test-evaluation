from solutions.task_011 import string_xor


def test_string_xor_empty():
    assert string_xor('', '') == ''


def test_string_xor_docstring_example():
    assert string_xor('010', '110') == '100'


def test_string_xor_all_zeros():
    assert string_xor('000', '000') == '000'


def test_string_xor_all_ones():
    assert string_xor('111', '111') == '000'


def test_string_xor_alternating():
    assert string_xor('1010', '0101') == '1111'


def test_string_xor_mixed():
    assert string_xor('1100', '1010') == '0110'