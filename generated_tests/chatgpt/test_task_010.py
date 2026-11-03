import pytest
from solutions.task_010 import make_palindrome


def test_empty_string():
    assert make_palindrome("") == ""


def test_docstring_example_cat():
    assert make_palindrome("cat") == "catac"


def test_docstring_example_cata():
    assert make_palindrome("cata") == "catac"


def test_single_character():
    assert make_palindrome("a") == "a"


def test_two_identical_characters():
    assert make_palindrome("aa") == "aa"


def test_two_different_characters():
    assert make_palindrome("ab") == "aba"


def test_already_palindrome():
    assert make_palindrome("racecar") == "racecar"


def test_even_length_palindrome():
    assert make_palindrome("abba") == "abba"


def test_odd_length_palindrome():
    assert make_palindrome("madam") == "madam"


def test_longest_palindromic_suffix():
    assert make_palindrome("abac") == "abacaba"


def test_palindromic_suffix_of_length_one():
    assert make_palindrome("abcd") == "abcdcba"


def test_palindromic_suffix_of_length_two():
    assert make_palindrome("aabb") == "aabbaa"


def test_palindromic_suffix_of_length_three():
    assert make_palindrome("ababc") == "abab c".replace(" ", "") + "aba"


def test_repeated_characters():
    assert make_palindrome("aaaa") == "aaaa"


def test_all_characters_different():
    assert make_palindrome("abcd") == "abcdcba"


def test_string_with_repeated_prefix():
    assert make_palindrome("aacecaaa") == "aacecaaa"


def test_string_with_spaces():
    assert make_palindrome("ab ba") == "ab ba"


def test_string_with_leading_spaces():
    assert make_palindrome(" ab") == " ab "


def test_string_with_trailing_spaces():
    assert make_palindrome("ab ") == "ab ba"


def test_case_sensitive_characters():
    assert make_palindrome("Aa") == "AaA"


def test_numeric_string():
    assert make_palindrome("123") == "12321"


def test_special_characters():
    assert make_palindrome("a!b") == "a!b!a"


def test_unicode_string():
    assert make_palindrome("café") == "caf éfac".replace(" ", "")


def test_result_is_palindrome():
    result = make_palindrome("python")
    assert result == result[::-1]


def test_result_starts_with_original_string():
    original = "hello"
    result = make_palindrome(original)
    assert result.startswith(original)


def test_shortest_palindrome_property():
    original = "abca"
    result = make_palindrome(original)
    assert result == "abcacba"


def test_already_palindromic_single_zero():
    assert make_palindrome("0") == "0"


def test_string_with_all_same_symbols():
    assert make_palindrome("!!!") == "!!!"


def test_longer_string():
    assert make_palindrome("abcdabc") == "abcdabcbadcba"