from solutions.task_010 import make_palindrome


def test_make_palindrome_empty_string():
    assert make_palindrome("") == ""


def test_make_palindrome_single_character():
    assert make_palindrome("a") == "a"


def test_make_palindrome_already_palindrome():
    assert make_palindrome("radar") == "radar"


def test_make_palindrome_docstring_examples():
    assert make_palindrome("cat") == "catac"
    assert make_palindrome("cata") == "catac"


def test_make_palindrome_partial_palindrome_at_end():
    assert make_palindrome("abcc") == "abccba"


def test_make_palindrome_no_repeating_chars():
    assert make_palindrome("abcd") == "abcdcba"