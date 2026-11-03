import pytest
from solutions.task_023 import strlen


def test_empty_string():
    assert strlen("") == 0


def test_docstring_example():
    assert strlen("abc") == 3


def test_single_character():
    assert strlen("a") == 1


def test_multiple_characters():
    assert strlen("hello world") == 11


def test_string_with_spaces():
    assert strlen("   ") == 3


def test_string_with_leading_and_trailing_spaces():
    assert strlen(" hello ") == 7


def test_string_with_digits():
    assert strlen("123456") == 6


def test_string_with_special_characters():
    assert strlen("!@#$%^&*()") == 10


def test_string_with_mixed_characters():
    assert strlen("Abc123! ") == 8


def test_string_with_newline():
    assert strlen("hello\nworld") == 11


def test_string_with_tab():
    assert strlen("a\tb") == 3


def test_unicode_characters():
    assert strlen("こんにちは") == 5


def test_repeated_characters():
    assert strlen("aaaaaa") == 6


def test_long_string():
    string = "a" * 10000
    assert strlen(string) == 10000


def test_string_with_emojis():
    assert strlen("😀😀😀") == 3


def test_string_with_combining_character():
    assert strlen("e\u0301") == 2


def test_string_with_quotes():
    assert strlen("'hello'") == 7


def test_string_with_only_punctuation():
    assert strlen("...!!!???") == 9


def test_return_type_is_integer():
    result = strlen("test")
    assert isinstance(result, int)


def test_length_preserves_all_whitespace():
    assert strlen(" \t\n ") == 4