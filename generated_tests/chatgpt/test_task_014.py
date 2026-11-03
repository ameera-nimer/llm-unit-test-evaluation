import pytest
from solutions.task_014 import all_prefixes


def test_empty_string():
    assert all_prefixes("") == []


def test_single_character():
    assert all_prefixes("a") == ["a"]


def test_docstring_example():
    assert all_prefixes("abc") == ["a", "ab", "abc"]


def test_two_character_string():
    assert all_prefixes("ab") == ["a", "ab"]


def test_longer_string():
    assert all_prefixes("hello") == ["h", "he", "hel", "hell", "hello"]


def test_all_identical_characters():
    assert all_prefixes("aaaa") == ["a", "aa", "aaa", "aaaa"]


def test_numeric_string():
    assert all_prefixes("1234") == ["1", "12", "123", "1234"]


def test_string_with_spaces():
    assert all_prefixes("a b") == ["a", "a ", "a b"]


def test_string_with_leading_space():
    assert all_prefixes(" abc") == [" ", " a", " ab", " abc"]


def test_string_with_trailing_space():
    assert all_prefixes("abc ") == ["a", "ab", "abc", "abc "]


def test_string_containing_special_characters():
    assert all_prefixes("a@#") == ["a", "a@", "a@#"]


def test_unicode_string():
    assert all_prefixes("café") == ["c", "ca", "caf", "café"]


def test_non_latin_string():
    assert all_prefixes("مرحبا") == ["م", "مر", "مرح", "مرحب", "مرحبا"]


def test_string_with_newline():
    assert all_prefixes("a\nb") == ["a", "a\n", "a\nb"]


def test_string_with_tab():
    assert all_prefixes("a\tb") == ["a", "a\t", "a\tb"]


def test_mixed_letters_and_numbers():
    assert all_prefixes("a1b2") == ["a", "a1", "a1b", "a1b2"]


def test_palindrome_string():
    assert all_prefixes("aba") == ["a", "ab", "aba"]


def test_prefixes_are_ordered_by_length():
    result = all_prefixes("python")
    assert result == ["p", "py", "pyt", "pyth", "pytho", "python"]


def test_number_of_prefixes_equals_string_length():
    string = "testing"
    assert len(all_prefixes(string)) == len(string)


def test_last_prefix_equals_original_string():
    string = "boundary"
    assert all_prefixes(string)[-1] == string


def test_every_prefix_is_a_prefix_of_original():
    string = "example"
    for prefix in all_prefixes(string):
        assert string.startswith(prefix)


def test_each_prefix_grows_by_one_character():
    result = all_prefixes("hello")
    for i in range(1, len(result)):
        assert len(result[i]) == len(result[i - 1]) + 1


def test_result_is_a_list():
    assert isinstance(all_prefixes("abc"), list)


def test_input_string_is_unchanged():
    string = "unchanged"
    original = string
    all_prefixes(string)
    assert string == original


def test_long_string():
    string = "a" * 1000
    result = all_prefixes(string)
    assert len(result) == 1000
    assert result[0] == "a"
    assert result[-1] == string