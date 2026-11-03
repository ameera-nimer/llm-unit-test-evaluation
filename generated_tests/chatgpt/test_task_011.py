import pytest
from solutions.task_011 import string_xor


def test_docstring_example():
    assert string_xor("010", "110") == "100"


def test_empty_strings():
    assert string_xor("", "") == ""


def test_first_string_empty():
    assert string_xor("", "101") == ""


def test_second_string_empty():
    assert string_xor("101", "") == ""


def test_single_zero_bits():
    assert string_xor("0", "0") == "0"


def test_single_one_bits():
    assert string_xor("1", "1") == "0"


def test_zero_xor_one():
    assert string_xor("0", "1") == "1"


def test_one_xor_zero():
    assert string_xor("1", "0") == "1"


def test_all_zeros():
    assert string_xor("0000", "0000") == "0000"


def test_all_ones():
    assert string_xor("1111", "1111") == "0000"


def test_zeros_xor_ones():
    assert string_xor("0000", "1111") == "1111"


def test_ones_xor_zeros():
    assert string_xor("1111", "0000") == "1111"


def test_alternating_bits():
    assert string_xor("0101", "1010") == "1111"


def test_identical_binary_strings():
    assert string_xor("101010", "101010") == "000000"


def test_complementary_binary_strings():
    assert string_xor("101010", "010101") == "111111"


def test_mixed_binary_strings():
    assert string_xor("11001", "10101") == "01100"


def test_result_length_matches_first_string_when_equal_lengths():
    a = "10101"
    b = "11011"
    assert len(string_xor(a, b)) == len(a)


def test_different_lengths_first_string_longer():
    assert string_xor("10110", "011") == "110"


def test_different_lengths_second_string_longer():
    assert string_xor("011", "10110") == "110"


def test_only_common_prefix_is_processed():
    assert string_xor("101", "11") == "01"


def test_single_character_against_longer_string():
    assert string_xor("1", "10101") == "0"


def test_long_binary_strings():
    a = "10101010101010101010"
    b = "01010101010101010101"
    assert string_xor(a, b) == "11111111111111111111"


def test_leading_zeros_are_preserved():
    assert string_xor("00101", "00011") == "00110"


def test_result_contains_only_binary_digits():
    result = string_xor("101101", "110011")
    assert all(bit in "01" for bit in result)


def test_xor_is_commutative():
    a = "101101"
    b = "011011"
    assert string_xor(a, b) == string_xor(b, a)


def test_xor_with_self_returns_zeros():
    a = "10110011"
    assert string_xor(a, a) == "00000000"


def test_xor_with_zeros_returns_original_string():
    a = "101101"
    assert string_xor(a, "000000") == a


def test_result_for_one_bit_difference():
    assert string_xor("1110", "1100") == "0010"


def test_large_input():
    a = "1" * 1000
    b = "0" * 1000
    assert string_xor(a, b) == "1" * 1000