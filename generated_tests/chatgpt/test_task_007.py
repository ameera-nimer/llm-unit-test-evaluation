import pytest
from solutions.task_007 import filter_by_substring


def test_empty_list():
    assert filter_by_substring([], "a") == []


def test_docstring_example():
    assert filter_by_substring(["abc", "bacd", "cde", "array"], "a") == [
        "abc", "bacd", "array"
    ]


def test_no_matching_strings():
    assert filter_by_substring(["hello", "world", "python"], "z") == []


def test_all_strings_match():
    assert filter_by_substring(["apple", "banana", "grape"], "a") == [
        "apple", "banana", "grape"
    ]


def test_single_matching_string():
    assert filter_by_substring(["hello"], "ell") == ["hello"]


def test_single_nonmatching_string():
    assert filter_by_substring(["hello"], "xyz") == []


def test_empty_substring():
    assert filter_by_substring(["abc", "def", "ghi"], "") == [
        "abc", "def", "ghi"
    ]


def test_empty_substring_with_empty_list():
    assert filter_by_substring([], "") == []


def test_empty_string_in_list():
    assert filter_by_substring(["", "abc", "", "a"], "a") == ["abc", "a"]


def test_empty_string_matches_empty_substring():
    assert filter_by_substring(["", "abc", ""], "") == ["", "abc", ""]


def test_exact_string_match():
    assert filter_by_substring(["cat", "dog", "bird"], "dog") == ["dog"]


def test_substring_at_start():
    assert filter_by_substring(["apple", "apricot", "banana"], "ap") == [
        "apple", "apricot"
    ]


def test_substring_at_end():
    assert filter_by_substring(["testing", "walking", "hello"], "ing") == [
        "testing", "walking"
    ]


def test_substring_in_middle():
    assert filter_by_substring(["abcde", "xabcy", "axyz"], "bc") == [
        "abcde", "xabcy"
    ]


def test_case_sensitive_matching():
    assert filter_by_substring(["Apple", "apple", "APPLE"], "apple") == [
        "apple"
    ]


def test_repeated_substring():
    assert filter_by_substring(["aaaa", "aaab", "bbbb"], "aa") == [
        "aaaa", "aaab"
    ]


def test_duplicate_strings_are_preserved():
    assert filter_by_substring(["apple", "banana", "apple"], "apple") == [
        "apple", "apple"
    ]


def test_original_order_is_preserved():
    assert filter_by_substring(["zebra", "apple", "mango", "avocado"], "a") == [
        "zebra", "apple", "mango", "avocado"
    ]


def test_substring_longer_than_all_strings():
    assert filter_by_substring(["a", "ab", "abc"], "abcd") == []


def test_multicharacter_substring():
    assert filter_by_substring(
        ["banana", "bandana", "cabana", "apple"], "ana"
    ) == ["banana", "bandana", "cabana"]


def test_special_characters():
    assert filter_by_substring(["a@b.com", "user#123", "a+b=c"], "+") == [
        "a+b=c"
    ]


def test_unicode_substring():
    assert filter_by_substring(["café", "coffee", "naïve"], "é") == ["café"]


def test_whitespace_substring():
    assert filter_by_substring(
        ["hello world", "helloworld", "good morning"], " "
    ) == ["hello world", "good morning"]


def test_string_containing_only_substring():
    assert filter_by_substring(["a", "b", "aa"], "a") == ["a", "aa"]


def test_substring_not_present_due_to_character_order():
    assert filter_by_substring(["abc", "acb", "bac"], "ab") == ["abc"]


def test_newline_substring():
    assert filter_by_substring(
        ["hello\nworld", "helloworld", "a\nb"], "\n"
    ) == ["hello\nworld", "a\nb"]


def test_numeric_characters_in_strings():
    assert filter_by_substring(["task007", "task008", "007task"], "007") == [
        "task007", "007task"
    ]