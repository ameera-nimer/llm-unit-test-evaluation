import pytest
from solutions.task_014 import all_prefixes


def test_docstring_example():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']


def test_empty_string():
    assert all_prefixes('') == []


def test_single_character():
    assert all_prefixes('a') == ['a']


def test_two_characters():
    assert all_prefixes('ab') == ['a', 'ab']


def test_four_characters():
    assert all_prefixes('abcd') == ['a', 'ab', 'abc', 'abcd']


def test_word():
    assert all_prefixes('hello') == ['h', 'he', 'hel', 'hell', 'hello']


def test_repeated_characters():
    assert all_prefixes('aaa') == ['a', 'aa', 'aaa']


def test_palindrome_input():
    assert all_prefixes('aba') == ['a', 'ab', 'aba']


def test_digits():
    assert all_prefixes('123') == ['1', '12', '123']


def test_spaces_included():
    assert all_prefixes('a b') == ['a', 'a ', 'a b']


def test_leading_space():
    assert all_prefixes(' a') == [' ', ' a']


def test_only_spaces():
    assert all_prefixes('   ') == [' ', '  ', '   ']


def test_special_characters():
    assert all_prefixes('!@#') == ['!', '!@', '!@#']


def test_newline_and_tab():
    assert all_prefixes('a\n\t') == ['a', 'a\n', 'a\n\t']


def test_case_preserved():
    assert all_prefixes('AbC') == ['A', 'Ab', 'AbC']


def test_unicode_characters():
    assert all_prefixes('éàü') == ['é', 'éà', 'éàü']


def test_unicode_emoji():
    assert all_prefixes('a😀b') == ['a', 'a😀', 'a😀b']


def test_length_equals_string_length():
    for s in ['', 'a', 'ab', 'abcdef', 'x' * 50]:
        assert len(all_prefixes(s)) == len(s)


def test_each_prefix_length_increases_by_one():
    result = all_prefixes('abcdefg')
    assert [len(p) for p in result] == list(range(1, 8))


def test_first_prefix_is_first_character():
    s = 'python'
    assert all_prefixes(s)[0] == s[0]


def test_last_prefix_is_whole_string():
    s = 'python'
    assert all_prefixes(s)[-1] == s


def test_every_prefix_is_prefix_of_input():
    s = 'abracadabra'
    assert all(s.startswith(p) for p in all_prefixes(s))


def test_each_prefix_extends_previous():
    result = all_prefixes('abcdef')
    for prev, curr in zip(result, result[1:]):
        assert curr.startswith(prev)
        assert len(curr) == len(prev) + 1


def test_ordered_shortest_to_longest():
    result = all_prefixes('abcdef')
    assert result == sorted(result, key=len)


def test_matches_reference_implementation():
    s = 'reference'
    expected = [s[:i] for i in range(1, len(s) + 1)]
    assert all_prefixes(s) == expected


def test_no_empty_prefix_included():
    assert '' not in all_prefixes('abc')


def test_all_prefixes_are_unique_in_length():
    result = all_prefixes('aaaa')
    assert len(set(result)) == 4


def test_long_string():
    s = 'a' * 1000
    result = all_prefixes(s)
    assert len(result) == 1000
    assert result[0] == 'a'
    assert result[-1] == s
    assert result[499] == 'a' * 500


def test_long_string_distinct_characters():
    s = ''.join(chr(ord('a') + i % 26) for i in range(500))
    result = all_prefixes(s)
    assert result == [s[:i] for i in range(1, 501)]


def test_returns_list_type():
    assert isinstance(all_prefixes('abc'), list)
    assert isinstance(all_prefixes(''), list)


def test_returns_list_of_strings():
    assert all(isinstance(p, str) for p in all_prefixes('abc'))


def test_empty_input_returns_new_list_each_call():
    first = all_prefixes('')
    second = all_prefixes('')
    assert first == second == []
    assert first is not second


def test_input_not_modified():
    s = 'abc'
    all_prefixes(s)
    assert s == 'abc'


def test_list_input_returns_list_prefixes():
    # slicing a list works the same way
    assert all_prefixes([1, 2, 3]) == [[1], [1, 2], [1, 2, 3]]


def test_non_sized_input_raises_type_error():
    with pytest.raises(TypeError):
        all_prefixes(123)


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        all_prefixes(None)


@pytest.mark.parametrize(
    "string, expected",
    [
        ('', []),
        ('a', ['a']),
        ('ab', ['a', 'ab']),
        ('abc', ['a', 'ab', 'abc']),
        ('aa', ['a', 'aa']),
        ('ba', ['b', 'ba']),
        ('xyz', ['x', 'xy', 'xyz']),
        ('12', ['1', '12']),
        (' a', [' ', ' a']),
        ('a b', ['a', 'a ', 'a b']),
        ('abcd', ['a', 'ab', 'abc', 'abcd']),
    ],
)
def test_parametrized_cases(string, expected):
    assert all_prefixes(string) == expected