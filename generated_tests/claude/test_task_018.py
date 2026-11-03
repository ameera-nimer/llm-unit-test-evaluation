import pytest
from solutions.task_018 import how_many_times


def test_docstring_example_empty_string():
    assert how_many_times('', 'a') == 0


def test_docstring_example_single_char_repeated():
    assert how_many_times('aaa', 'a') == 3


def test_docstring_example_overlapping():
    assert how_many_times('aaaa', 'aa') == 3


def test_both_empty_strings():
    # range(0 - 0 + 1) -> one iteration, '' == '' -> 1
    assert how_many_times('', '') == 1


def test_empty_substring_counts_len_plus_one():
    assert how_many_times('abc', '') == 4


def test_empty_substring_single_char_string():
    assert how_many_times('a', '') == 2


def test_no_occurrences():
    assert how_many_times('abcdef', 'xyz') == 0


def test_single_occurrence():
    assert how_many_times('abcdef', 'cd') == 1


def test_multiple_non_overlapping_occurrences():
    assert how_many_times('abcabcabc', 'abc') == 3


def test_overlapping_occurrences_three_chars():
    assert how_many_times('aaaaa', 'aaa') == 3


def test_overlapping_pattern_ababa():
    assert how_many_times('ababababa', 'aba') == 4


def test_overlapping_pattern_abab():
    assert how_many_times('abababab', 'abab') == 3


def test_substring_equals_string():
    assert how_many_times('hello', 'hello') == 1


def test_substring_longer_than_string():
    assert how_many_times('ab', 'abc') == 0


def test_substring_longer_than_string_by_one():
    assert how_many_times('abc', 'abcd') == 0


def test_substring_much_longer_than_string():
    assert how_many_times('a', 'a' * 100) == 0


def test_empty_string_with_longer_substring():
    assert how_many_times('', 'abc') == 0


def test_single_char_string_matching():
    assert how_many_times('a', 'a') == 1


def test_single_char_string_not_matching():
    assert how_many_times('a', 'b') == 0


def test_match_at_start_only():
    assert how_many_times('abxxxx', 'ab') == 1


def test_match_at_end_only():
    assert how_many_times('xxxxab', 'ab') == 1


def test_match_at_both_ends():
    assert how_many_times('abxxab', 'ab') == 2


def test_match_in_middle_only():
    assert how_many_times('xxabxx', 'ab') == 1


def test_last_possible_position_is_checked():
    assert how_many_times('xxxab', 'ab') == 1
    assert how_many_times('xxxa', 'ab') == 0


def test_case_sensitive():
    assert how_many_times('aAaA', 'a') == 2
    assert how_many_times('aAaA', 'A') == 2
    assert how_many_times('aAaA', 'aA') == 2


def test_case_sensitive_no_match():
    assert how_many_times('HELLO', 'hello') == 0


def test_spaces_in_string_and_substring():
    assert how_many_times('a b a b a', 'a b') == 2


def test_whitespace_substring():
    assert how_many_times('a b c d', ' ') == 3


def test_special_characters_literal():
    assert how_many_times('a.b.c.d', '.') == 3


def test_regex_metacharacters_treated_literally():
    assert how_many_times('a*b*c', '*') == 2
    assert how_many_times('abc', 'a.c') == 0


def test_newline_characters():
    assert how_many_times('a\nb\nc', '\n') == 2


def test_digits():
    assert how_many_times('1212121', '121') == 3


def test_unicode_characters():
    assert how_many_times('ééé', 'é') == 3


def test_unicode_overlapping():
    assert how_many_times('ééé', 'éé') == 2


def test_emoji():
    assert how_many_times('😀😀😀', '😀😀') == 2


def test_all_same_char_count_formula():
    for n in range(1, 20):
        for k in range(1, n + 1):
            assert how_many_times('a' * n, 'a' * k) == n - k + 1


def test_single_char_count_matches_str_count():
    for s in ['banana', 'mississippi', 'hello world', 'aaaaaa']:
        for ch in set(s):
            assert how_many_times(s, ch) == s.count(ch)


def test_non_overlapping_matches_str_count():
    s = 'abcabcxabc'
    assert how_many_times(s, 'abc') == s.count('abc')


def test_matches_reference_implementation():
    def reference(s, sub):
        return sum(1 for i in range(len(s) - len(sub) + 1) if s.startswith(sub, i))

    cases = [
        ('banana', 'ana'),
        ('aaaa', 'aa'),
        ('abababa', 'aba'),
        ('mississippi', 'issi'),
        ('abc', 'd'),
        ('xyz', 'xyz'),
    ]
    for s, sub in cases:
        assert how_many_times(s, sub) == reference(s, sub)


def test_result_never_exceeds_max_positions():
    s = 'abcabcabc'
    sub = 'bc'
    assert how_many_times(s, sub) <= len(s) - len(sub) + 1


def test_result_is_non_negative():
    for s, sub in [('', 'a'), ('a', 'abc'), ('abc', 'abcd'), ('abc', 'b')]:
        assert how_many_times(s, sub) >= 0


def test_long_string_single_char():
    assert how_many_times('a' * 10000, 'a') == 10000


def test_long_string_overlapping():
    assert how_many_times('a' * 10000, 'aa') == 9999


def test_long_string_no_match():
    assert how_many_times('a' * 10000, 'b') == 0


def test_long_string_periodic_pattern():
    assert how_many_times('ab' * 1000, 'ab') == 1000
    assert how_many_times('ab' * 1000, 'ba') == 999


def test_long_substring_in_long_string():
    needle = 'xyz' * 50
    haystack = 'a' * 100 + needle + 'b' * 100
    assert how_many_times(haystack, needle) == 1


def test_returns_int_type():
    assert isinstance(how_many_times('aaa', 'a'), int)
    assert isinstance(how_many_times('', 'a'), int)


def test_inputs_not_modified():
    s, sub = 'aaaa', 'aa'
    how_many_times(s, sub)
    assert s == 'aaaa'
    assert sub == 'aa'


def test_non_string_substring_raises_type_error():
    with pytest.raises(TypeError):
        how_many_times('abc', 1)


def test_none_string_raises_type_error():
    with pytest.raises(TypeError):
        how_many_times(None, 'a')


def test_none_substring_raises_type_error():
    with pytest.raises(TypeError):
        how_many_times('abc', None)


@pytest.mark.parametrize(
    "string, substring, expected",
    [
        ('', 'a', 0),
        ('', '', 1),
        ('a', '', 2),
        ('a', 'a', 1),
        ('a', 'b', 0),
        ('aaa', 'a', 3),
        ('aaaa', 'aa', 3),
        ('aaaa', 'aaa', 2),
        ('aaaa', 'aaaa', 1),
        ('aaaa', 'aaaaa', 0),
        ('abab', 'ab', 2),
        ('ababa', 'aba', 2),
        ('abcabc', 'abc', 2),
        ('abcabc', 'ca', 1),
        ('banana', 'ana', 2),
        ('banana', 'na', 2),
        ('mississippi', 'ss', 2),
        ('mississippi', 'issi', 2),
        ('hello world', 'o', 2),
        ('hello world', 'xyz', 0),
    ],
)
def test_parametrized_cases(string, substring, expected):
    assert how_many_times(string, substring) == expected