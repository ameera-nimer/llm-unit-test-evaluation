import pytest
from solutions.task_007 import filter_by_substring


def test_docstring_example_empty():
    assert filter_by_substring([], 'a') == []


def test_docstring_example_multiple_matches():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']


def test_no_matches():
    assert filter_by_substring(['abc', 'def', 'ghi'], 'z') == []


def test_all_match():
    assert filter_by_substring(['apple', 'banana', 'grape'], 'a') == ['apple', 'banana', 'grape']


def test_single_match():
    assert filter_by_substring(['abc', 'def', 'ghi'], 'e') == ['def']


def test_single_element_list_match():
    assert filter_by_substring(['hello'], 'ell') == ['hello']


def test_single_element_list_no_match():
    assert filter_by_substring(['hello'], 'xyz') == []


def test_substring_at_start():
    assert filter_by_substring(['hello', 'world', 'help'], 'hel') == ['hello', 'help']


def test_substring_at_end():
    assert filter_by_substring(['running', 'jumping', 'cat'], 'ing') == ['running', 'jumping']


def test_substring_in_middle():
    assert filter_by_substring(['abcde', 'xbcdy', 'bc'], 'bcd') == ['abcde', 'xbcdy']


def test_substring_equals_whole_string():
    assert filter_by_substring(['abc', 'abcd', 'ab'], 'abc') == ['abc', 'abcd']


def test_substring_longer_than_strings():
    assert filter_by_substring(['a', 'ab', 'abc'], 'abcd') == []


def test_empty_substring_matches_everything():
    assert filter_by_substring(['a', 'b', 'c'], '') == ['a', 'b', 'c']


def test_empty_substring_matches_empty_strings():
    assert filter_by_substring(['', 'a', ''], '') == ['', 'a', '']


def test_empty_substring_with_empty_list():
    assert filter_by_substring([], '') == []


def test_empty_strings_in_list_with_nonempty_substring():
    assert filter_by_substring(['', 'a', '', 'ab'], 'a') == ['a', 'ab']


def test_case_sensitive_lowercase_substring():
    assert filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']


def test_case_sensitive_uppercase_substring():
    assert filter_by_substring(['Apple', 'apple', 'APPLE'], 'APPLE') == ['APPLE']


def test_whitespace_substring():
    assert filter_by_substring(['hello world', 'helloworld', 'a b'], ' ') == ['hello world', 'a b']


def test_special_characters_substring():
    assert filter_by_substring(['a.b', 'ab', 'a*b', 'a.b.c'], '.') == ['a.b', 'a.b.c']


def test_regex_characters_treated_literally():
    assert filter_by_substring(['abc', 'a.c', 'a*c'], 'a.c') == ['a.c']


def test_numeric_characters():
    assert filter_by_substring(['abc123', 'def456', '789'], '45') == ['def456']


def test_unicode_substring():
    assert filter_by_substring(['café', 'cafe', 'naïve'], 'é') == ['café']


def test_duplicate_strings_preserved():
    assert filter_by_substring(['abc', 'abc', 'def', 'abc'], 'abc') == ['abc', 'abc', 'abc']


def test_order_preserved():
    assert filter_by_substring(['zebra', 'apple', 'mango', 'banana'], 'a') == [
        'zebra', 'apple', 'mango', 'banana'
    ]


def test_overlapping_pattern():
    assert filter_by_substring(['aaa', 'aa', 'a'], 'aa') == ['aaa', 'aa']


def test_repeated_substring_in_string():
    assert filter_by_substring(['abab', 'ab', 'ba'], 'ab') == ['abab', 'ab']


def test_newline_in_strings():
    assert filter_by_substring(['a\nb', 'ab', 'a\n'], '\n') == ['a\nb', 'a\n']


def test_result_is_list_of_strings():
    result = filter_by_substring(['abc', 'bcd'], 'b')
    assert isinstance(result, list)
    assert all(isinstance(s, str) for s in result)


def test_result_is_subset_of_input():
    strings = ['abc', 'def', 'bcd', 'xyz']
    result = filter_by_substring(strings, 'b')
    assert all(s in strings for s in result)


def test_all_results_contain_substring():
    result = filter_by_substring(['abc', 'bcd', 'xyz', 'cab'], 'ab')
    assert all('ab' in s for s in result)


def test_input_list_not_modified():
    strings = ['abc', 'def', 'bcd']
    original = list(strings)
    filter_by_substring(strings, 'b')
    assert strings == original


def test_returns_new_list_object():
    strings = ['abc', 'abd']
    result = filter_by_substring(strings, 'ab')
    assert result == strings
    assert result is not strings


def test_tuple_input_works():
    assert filter_by_substring(('abc', 'def', 'bcd'), 'b') == ['abc', 'bcd']


def test_large_list():
    strings = ['item' + str(i) for i in range(1000)]
    result = filter_by_substring(strings, '99')
    expected = [s for s in strings if '99' in s]
    assert result == expected


def test_long_strings():
    long_string = 'a' * 10000 + 'needle' + 'b' * 10000
    assert filter_by_substring([long_string, 'a' * 100], 'needle') == [long_string]


def test_non_string_substring_raises_type_error():
    with pytest.raises(TypeError):
        filter_by_substring(['abc', 'def'], 1)


@pytest.mark.parametrize(
    "strings, substring, expected",
    [
        ([], 'a', []),
        (['a'], 'a', ['a']),
        (['a'], 'b', []),
        (['abc', 'bcd', 'cde'], 'bc', ['abc', 'bcd']),
        (['abc', 'bcd', 'cde'], 'cd', ['bcd', 'cde']),
        (['abc', 'bcd', 'cde'], '', ['abc', 'bcd', 'cde']),
        (['Hello', 'hello'], 'H', ['Hello']),
        (['one', 'two', 'three'], 'e', ['one', 'three']),
        (['x', 'xx', 'xxx'], 'xx', ['xx', 'xxx']),
    ],
)
def test_parametrized_cases(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected