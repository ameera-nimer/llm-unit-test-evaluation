import pytest
from solutions.task_012 import longest


def test_empty_list():
    assert longest([]) is None


def test_single_string():
    assert longest(["hello"]) == "hello"


def test_single_empty_string():
    assert longest([""]) == ""


def test_docstring_example_equal_lengths():
    assert longest(["a", "b", "c"]) == "a"


def test_docstring_example_different_lengths():
    assert longest(["a", "bb", "ccc"]) == "ccc"


def test_first_string_is_longest():
    assert longest(["elephant", "cat", "dog"]) == "elephant"


def test_last_string_is_longest():
    assert longest(["cat", "dog", "elephant"]) == "elephant"


def test_middle_string_is_longest():
    assert longest(["cat", "elephant", "dog"]) == "elephant"


def test_multiple_strings_with_same_maximum_length():
    assert longest(["apple", "grape", "mango"]) == "apple"


def test_first_longest_string_is_returned():
    assert longest(["abc", "defgh", "12345", "xyz"]) == "defgh"


def test_all_strings_have_equal_length():
    assert longest(["abc", "def", "ghi"]) == "abc"


def test_all_strings_are_empty():
    assert longest(["", "", ""]) == ""


def test_empty_string_and_nonempty_strings():
    assert longest(["", "a", ""]) == "a"


def test_empty_string_does_not_override_longest():
    assert longest(["", "hello", ""]) == "hello"


def test_strings_with_spaces():
    assert longest(["hello world", "hello", "world"]) == "hello world"


def test_string_with_whitespace_only():
    assert longest([" ", "  ", "a"]) == "  "


def test_strings_with_special_characters():
    assert longest(["!@#", "abcdef", "$%^&"]) == "abcdef"


def test_strings_with_numbers():
    assert longest(["123", "12345", "12"]) == "12345"


def test_unicode_strings():
    assert longest(["cat", "café", "你好世界"]) == "你好世界"


def test_string_with_newline():
    assert longest(["abc", "a\nb\nc\nd", "xyz"]) == "a\nb\nc\nd"


def test_case_sensitive_strings():
    assert longest(["ABC", "abcd", "AbCd"]) == "abcd"


def test_duplicate_longest_strings():
    assert longest(["longest", "short", "longest"]) == "longest"


def test_first_duplicate_longest_string_is_returned():
    assert longest(["abcde", "12345", "xyz"]) == "abcde"


def test_longest_string_at_beginning_with_tie():
    assert longest(["abcdef", "ghijkl", "abc"]) == "abcdef"


def test_longest_string_at_end_with_tie():
    assert longest(["abc", "defgh", "12345"]) == "defgh"


def test_list_with_two_strings():
    assert longest(["cat", "elephant"]) == "elephant"


def test_list_with_two_equal_length_strings():
    assert longest(["first", "other"]) == "first"


def test_very_long_string():
    long_string = "a" * 10000
    assert longest(["short", long_string, "medium"]) == long_string


def test_result_is_none_only_for_empty_list():
    assert longest([]) is None
    assert longest([""]) == ""


def test_input_list_is_not_modified():
    strings = ["cat", "elephant", "dog"]
    original = strings.copy()
    longest(strings)
    assert strings == original


def test_returns_original_string_not_modified():
    strings = ["abc", "longest", "xyz"]
    result = longest(strings)
    assert result is strings[1]