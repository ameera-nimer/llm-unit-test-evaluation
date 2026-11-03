import pytest
from solutions.task_010 import make_palindrome, is_palindrome


def test_docstring_example_empty():
    assert make_palindrome('') == ''


def test_docstring_example_cat():
    assert make_palindrome('cat') == 'catac'


def test_docstring_example_cata():
    assert make_palindrome('cata') == 'catac'


def test_single_character():
    assert make_palindrome('a') == 'a'


def test_two_identical_characters():
    assert make_palindrome('aa') == 'aa'


def test_two_different_characters():
    assert make_palindrome('ab') == 'aba'


def test_already_palindrome_odd_length():
    assert make_palindrome('racecar') == 'racecar'


def test_already_palindrome_even_length():
    assert make_palindrome('abba') == 'abba'


def test_all_identical_characters():
    assert make_palindrome('aaaa') == 'aaaa'


def test_no_palindromic_suffix_longer_than_one():
    assert make_palindrome('abcd') == 'abcdcba'


def test_palindromic_suffix_of_length_two():
    assert make_palindrome('abcc') == 'abccba'


def test_palindromic_suffix_of_length_three():
    assert make_palindrome('xabcbc') == 'xabcbcbax'[:0] + 'xabcbcbax'[:0] + make_palindrome('xabcbc')


def test_palindromic_suffix_length_three_explicit():
    # longest palindromic suffix of 'xyabа' style: 'abxbx' -> suffix 'xbx'
    assert make_palindrome('abxbx') == 'abxbxba'


def test_suffix_is_palindrome_prefix_one_char():
    assert make_palindrome('baa') == 'baab'


def test_suffix_is_palindrome_prefix_two_chars():
    assert make_palindrome('cbaa') == 'cbaabc'


def test_prefix_palindrome_but_not_suffix():
    # 'aab' starts with palindrome 'aa' but the longest palindromic suffix is 'b'
    assert make_palindrome('aab') == 'aabaa'


def test_longest_suffix_chosen_not_shortest():
    # suffixes: 'abaab' no, 'baab' yes -> append 'a'
    assert make_palindrome('abaab') == 'abaaba'


def test_repeated_pattern():
    assert make_palindrome('abab') == 'ababa'


def test_repeated_pattern_odd():
    assert make_palindrome('ababa') == 'ababa'


def test_with_spaces():
    assert make_palindrome('a b') == 'a b a'


def test_with_digits():
    assert make_palindrome('123') == '12321'


def test_with_punctuation():
    assert make_palindrome('a!') == 'a!a'


def test_case_sensitive():
    assert make_palindrome('Aa') == 'AaA'


def test_unicode_characters():
    assert make_palindrome('éa') == 'éaé'


def test_result_starts_with_input():
    for s in ['', 'a', 'ab', 'abc', 'abca', 'hello', 'level', 'python']:
        assert make_palindrome(s).startswith(s)


def test_result_is_palindrome():
    for s in ['', 'a', 'ab', 'abc', 'abca', 'hello', 'level', 'python', 'xyzzy']:
        result = make_palindrome(s)
        assert result == result[::-1]


def test_result_is_shortest_palindrome():
    # Brute-force check: no shorter palindrome starting with s exists
    def brute(s):
        if not s:
            return ''
        for k in range(len(s) + 1):
            candidate = s + s[:k][::-1]
            if candidate == candidate[::-1]:
                return candidate

    for s in ['', 'a', 'ab', 'aba', 'abc', 'abca', 'aabb', 'abcba', 'abcdef', 'xyzzyx', 'xyzzy']:
        assert make_palindrome(s) == brute(s)


def test_result_length_bounds():
    for s in ['a', 'ab', 'abc', 'abcd', 'abcde']:
        result = make_palindrome(s)
        assert len(s) <= len(result) <= 2 * len(s) - 1


def test_worst_case_length():
    s = 'abcdefgh'
    result = make_palindrome(s)
    assert len(result) == 2 * len(s) - 1
    assert result == 'abcdefghgfedcba'


def test_idempotent_on_result():
    for s in ['', 'a', 'ab', 'abc', 'abca', 'hello']:
        once = make_palindrome(s)
        assert make_palindrome(once) == once


def test_returns_str_type():
    assert isinstance(make_palindrome(''), str)
    assert isinstance(make_palindrome('abc'), str)


def test_long_palindrome_input_unchanged():
    s = 'a' * 500 + 'b' + 'a' * 500
    assert make_palindrome(s) == s


def test_long_string_no_palindromic_suffix():
    s = 'ab' * 100 + 'c'
    result = make_palindrome(s)
    assert result == s + s[:-1][::-1]
    assert result == result[::-1]


def test_long_string_of_distinct_characters():
    s = ''.join(chr(ord('a') + i) for i in range(26))
    result = make_palindrome(s)
    assert result == s + s[:-1][::-1]
    assert len(result) == 51


def test_non_string_input_raises_error():
    with pytest.raises(TypeError):
        make_palindrome(123)


def test_is_palindrome_helper_true_cases():
    assert is_palindrome('') is True
    assert is_palindrome('a') is True
    assert is_palindrome('aba') is True
    assert is_palindrome('abba') is True


def test_is_palindrome_helper_false_cases():
    assert is_palindrome('ab') is False
    assert is_palindrome('abca') is False
    assert is_palindrome('Aa') is False


@pytest.mark.parametrize(
    "string, expected",
    [
        ('', ''),
        ('a', 'a'),
        ('aa', 'aa'),
        ('ab', 'aba'),
        ('aba', 'aba'),
        ('abc', 'abcba'),
        ('abb', 'abba'),
        ('aab', 'aabaa'),
        ('cat', 'catac'),
        ('cata', 'catac'),
        ('race', 'racecar'),
        ('level', 'level'),
        ('abcd', 'abcdcba'),
        ('abcc', 'abccba'),
        ('xyx', 'xyx'),
        ('xyxz', 'xyxzxyx'),
    ],
)
def test_parametrized_cases(string, expected):
    assert make_palindrome(string) == expected