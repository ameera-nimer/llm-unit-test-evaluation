import pytest
from solutions.task_011 import string_xor


def test_docstring_example():
    assert string_xor('010', '110') == '100'


def test_empty_strings():
    assert string_xor('', '') == ''


def test_single_char_zero_zero():
    assert string_xor('0', '0') == '0'


def test_single_char_zero_one():
    assert string_xor('0', '1') == '1'


def test_single_char_one_zero():
    assert string_xor('1', '0') == '1'


def test_single_char_one_one():
    assert string_xor('1', '1') == '0'


def test_all_zeros():
    assert string_xor('0000', '0000') == '0000'


def test_all_ones():
    assert string_xor('1111', '1111') == '0000'


def test_zeros_xor_ones():
    assert string_xor('0000', '1111') == '1111'


def test_ones_xor_zeros():
    assert string_xor('1111', '0000') == '1111'


def test_alternating_patterns():
    assert string_xor('1010', '0101') == '1111'


def test_identical_strings_give_all_zeros():
    s = '1011001'
    assert string_xor(s, s) == '0' * len(s)


def test_xor_with_zeros_is_identity():
    s = '1011001'
    assert string_xor(s, '0' * len(s)) == s


def test_xor_with_ones_is_bitwise_complement():
    s = '1011001'
    expected = ''.join('0' if c == '1' else '1' for c in s)
    assert string_xor(s, '1' * len(s)) == expected


def test_commutative():
    a, b = '110010', '101101'
    assert string_xor(a, b) == string_xor(b, a)


def test_associative():
    a, b, c = '110010', '101101', '011011'
    assert string_xor(string_xor(a, b), c) == string_xor(a, string_xor(b, c))


def test_self_inverse():
    a, b = '110010', '101101'
    assert string_xor(string_xor(a, b), b) == a


def test_preserves_leading_zeros():
    assert string_xor('0011', '0001') == '0010'


def test_result_all_leading_zeros_preserved():
    assert string_xor('0101', '0101') == '0000'


def test_result_length_equals_input_length():
    a, b = '1100110011', '1010101010'
    assert len(string_xor(a, b)) == len(a)


def test_result_contains_only_binary_digits():
    result = string_xor('110101', '011011')
    assert set(result) <= {'0', '1'}


def test_returns_str_type():
    assert isinstance(string_xor('01', '10'), str)
    assert isinstance(string_xor('', ''), str)


def test_mixed_example():
    assert string_xor('101010', '110011') == '011001'


def test_long_strings():
    a = '10' * 500
    b = '01' * 500
    assert string_xor(a, b) == '1' * 1000


def test_long_identical_strings():
    a = '1101' * 250
    assert string_xor(a, a) == '0' * 1000


def test_different_lengths_first_longer_truncates():
    # zip stops at the shorter input
    assert string_xor('1010', '11') == '01'


def test_different_lengths_second_longer_truncates():
    assert string_xor('11', '1010') == '01'


def test_one_empty_string_returns_empty():
    assert string_xor('', '101') == ''
    assert string_xor('101', '') == ''


def test_non_binary_characters_treated_as_unequal():
    # any differing characters yield '1', identical ones yield '0'
    assert string_xor('ab', 'aa') == '01'


def test_inputs_not_modified():
    a, b = '1010', '0110'
    string_xor(a, b)
    assert a == '1010'
    assert b == '0110'


def test_non_iterable_input_raises_type_error():
    with pytest.raises(TypeError):
        string_xor(101, '101')


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ('', '', ''),
        ('0', '0', '0'),
        ('0', '1', '1'),
        ('1', '0', '1'),
        ('1', '1', '0'),
        ('00', '00', '00'),
        ('01', '10', '11'),
        ('11', '11', '00'),
        ('10', '11', '01'),
        ('010', '110', '100'),
        ('111', '000', '111'),
        ('1001', '0110', '1111'),
        ('1100', '1010', '0110'),
    ],
)
def test_parametrized_cases(a, b, expected):
    assert string_xor(a, b) == expected