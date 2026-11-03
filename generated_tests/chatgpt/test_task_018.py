import pytest
from solutions.task_018 import how_many_times


def test_empty_string():
    assert how_many_times("", "a") == 0


def test_single_character_occurrence():
    assert how_many_times("aaa", "a") == 3


def test_overlapping_occurrences():
    assert how_many_times("aaaa", "aa") == 3


def test_no_occurrences():
    assert how_many_times("abcdef", "x") == 0


def test_substring_equals_string():
    assert how_many_times("hello", "hello") == 1


def test_substring_longer_than_string():
    assert how_many_times("hi", "hello") == 0


def test_substring_at_start():
    assert how_many_times("abcdef", "abc") == 1


def test_substring_at_end():
    assert how_many_times("abcdef", "def") == 1


def test_multiple_non_overlapping_occurrences():
    assert how_many_times("abcabcabc", "abc") == 3


def test_repeated_overlapping_occurrences():
    assert how_many_times("aaaaa", "aaa") == 3


def test_single_character_string_and_substring():
    assert how_many_times("a", "a") == 1


def test_empty_substring():
    assert how_many_times("abc", "") == 4


def test_both_strings_empty():
    assert how_many_times("", "") == 1


def test_case_sensitive_matching():
    assert how_many_times("AaAa", "aa") == 0


def test_case_sensitive_matching_with_occurrences():
    assert how_many_times("AbAbAb", "Ab") == 3


def test_substring_with_spaces():
    assert how_many_times("a b a b", "a b") == 2


def test_special_characters():
    assert how_many_times("!@#!@#!@#", "!@#") == 3


def test_digits():
    assert how_many_times("121212", "12") == 3


def test_substring_occurring_at_every_position():
    assert how_many_times("aaaaaa", "a") == 6


def test_long_string_with_no_match():
    assert how_many_times("a" * 1000, "b") == 0