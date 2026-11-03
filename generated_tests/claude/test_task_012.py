import pytest
from solutions.task_012 import longest


def test_docstring_example_empty():
    assert longest([]) is None


def test_docstring_example_all_same_length():
    assert longest(['a', 'b', 'c']) == 'a'


def test_docstring_example_increasing_length():
    assert longest(['a', 'bb', 'ccc']) == 'ccc'


def test_single_element():
    assert longest(['hello']) == 'hello'


def test_single_empty_string():
    assert longest(['']) == ''


def test_all_empty_strings_returns_first():
    assert longest(['', '', '']) == ''


def test_two_elements_first_longer():
    assert longest(['abc', 'a']) == 'abc'


def test_two_elements_second_longer():
    assert longest(['a', 'abc']) == 'abc'


def test_longest_at_start():
    assert longest(['abcd', 'ab', 'a']) == 'abcd'


def test_longest_in_middle():
    assert longest(['a', 'abcd', 'ab']) == 'abcd'


def test_longest_at_end():
    assert longest(['a', 'ab', 'abcd']) == 'abcd'


def test_tie_returns_first_of_longest():
    assert longest(['aa', 'bb', 'cc']) == 'aa'


def test_tie_for_longest_not_at_start():
    assert longest(['a', 'bbb', 'ccc', 'dd']) == 'bbb'


def test_tie_for_longest_at_end():
    assert longest(['a', 'bb', 'ccc', 'ddd']) == 'ccc'


def test_tie_returns_first_even_if_identical_content_elsewhere():
    result = longest(['xyz', 'abc', 'xyz'])
    assert result == 'xyz'


def test_tie_between_first_and_last():
    assert longest(['abc', 'a', 'def']) == 'abc'


def test_returns_same_object_as_first_longest():
    first = 'abc'
    second = 'def'
    result = longest([first, second])
    assert result is first


def test_empty_string_among_nonempty():
    assert longest(['', 'a', '']) == 'a'


def test_empty_string_first_then_longer():
    assert longest(['', 'abc']) == 'abc'


def test_strings_with_spaces_counted():
    assert longest(['ab', 'a b', 'abc']) == 'a b'


def test_whitespace_only_string_counts_by_length():
    assert longest(['abc', '     ']) == '     '


def test_newline_and_tab_characters_count():
    assert longest(['ab', 'a\n\t']) == 'a\n\t'


def test_unicode_strings():
    assert longest(['é', 'éé', 'é']) == 'éé'


def test_length_counted_in_code_points():
    assert longest(['ab', 'é', 'abc']) == 'abc'


def test_digits_and_symbols():
    assert longest(['123', '!@#$', 'ab']) == '!@#$'


def test_case_does_not_matter_for_length():
    assert longest(['ABC', 'abcd', 'AB']) == 'abcd'


def test_duplicate_strings():
    assert longest(['abc', 'abc', 'abc']) == 'abc'


def test_long_strings():
    short = 'a' * 100
    long_ = 'b' * 10000
    assert longest([short, long_, short]) == long_


def test_long_list_longest_at_end():
    strings = ['a' * i for i in range(1, 1001)]
    assert longest(strings) == 'a' * 1000


def test_long_list_longest_at_start():
    strings = ['a' * i for i in range(1000, 0, -1)]
    assert longest(strings) == 'a' * 1000


def test_long_list_all_same_length_returns_first():
    strings = [str(i).zfill(4) for i in range(1000)]
    assert longest(strings) == '0000'


def test_result_is_element_of_input():
    strings = ['ab', 'abcde', 'abc']
    assert longest(strings) in strings


def test_result_has_maximum_length():
    strings = ['ab', 'abcde', 'abc', 'xyzzy']
    result = longest(strings)
    assert len(result) == max(len(s) for s in strings)


def test_matches_reference_implementation():
    strings = ['x', 'yy', 'zzz', 'www', 'v']
    expected = max(strings, key=len)  # max returns first maximal element
    assert longest(strings) == expected


def test_input_list_not_modified():
    strings = ['a', 'abc', 'ab']
    original = list(strings)
    longest(strings)
    assert strings == original


def test_returns_str_for_non_empty_input():
    assert isinstance(longest(['a', 'bb']), str)


def test_returns_none_type_for_empty_input():
    assert type(longest([])) is type(None)


def test_tuple_input_works():
    assert longest(('a', 'bbb', 'cc')) == 'bbb'


def test_non_sized_element_raises_type_error():
    with pytest.raises(TypeError):
        longest(['abc', 5])


@pytest.mark.parametrize(
    "strings, expected",
    [
        ([], None),
        ([''], ''),
        (['a'], 'a'),
        (['a', 'b'], 'a'),
        (['a', 'bb'], 'bb'),
        (['bb', 'a'], 'bb'),
        (['aa', 'bb'], 'aa'),
        (['a', 'bb', 'cc'], 'bb'),
        (['a', 'bb', 'ccc'], 'ccc'),
        (['ccc', 'bb', 'a'], 'ccc'),
        (['', 'a', ''], 'a'),
        (['abc', 'def', 'gh'], 'abc'),
        (['x', 'yy', 'zzz', 'www'], 'zzz'),
    ],
)
def test_parametrized_cases(strings, expected):
    assert longest(strings) == expected