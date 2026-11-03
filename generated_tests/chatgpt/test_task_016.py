import pytest
from solutions.task_016 import count_distinct_characters


def test_empty_string():
    assert count_distinct_characters("") == 0


def test_all_distinct_characters():
    assert count_distinct_characters("xyz") == 3


def test_repeated_characters():
    assert count_distinct_characters("aaaa") == 1


def test_case_insensitive_characters():
    assert count_distinct_characters("xyzXYZ") == 3


def test_docstring_example_jerry():
    assert count_distinct_characters("Jerry") == 4


def test_mixed_case_repeated_characters():
    assert count_distinct_characters("AaBbCc") == 3


def test_single_character():
    assert count_distinct_characters("a") == 1


def test_single_uppercase_character():
    assert count_distinct_characters("Z") == 1


def test_string_with_spaces():
    assert count_distinct_characters("a a") == 2


def test_string_with_punctuation():
    assert count_distinct_characters("!!??") == 2


def test_string_with_digits():
    assert count_distinct_characters("112233") == 3


def test_mixed_letters_digits_and_symbols():
    assert count_distinct_characters("Aa1!a1?") == 4


def test_whitespace_characters():
    assert count_distinct_characters("   ") == 1


def test_unicode_characters():
    assert count_distinct_characters("éÉ") == 1


def test_all_unique_mixed_characters():
    assert count_distinct_characters("Ab3!cD") == 6


def test_return_type_is_integer():
    result = count_distinct_characters("abc")
    assert isinstance(result, int)