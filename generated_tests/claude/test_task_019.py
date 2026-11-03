import pytest
from solutions.task_019 import sort_numbers

WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def test_docstring_example():
    assert sort_numbers('three one five') == 'one three five'


def test_empty_string():
    assert sort_numbers('') == ''


def test_only_spaces():
    assert sort_numbers('     ') == ''


def test_single_word_zero():
    assert sort_numbers('zero') == 'zero'


def test_single_word_nine():
    assert sort_numbers('nine') == 'nine'


def test_single_word_middle():
    assert sort_numbers('five') == 'five'


def test_two_words_already_sorted():
    assert sort_numbers('one two') == 'one two'


def test_two_words_reversed():
    assert sort_numbers('two one') == 'one two'


def test_boundary_zero_and_nine_sorted():
    assert sort_numbers('zero nine') == 'zero nine'


def test_boundary_zero_and_nine_reversed():
    assert sort_numbers('nine zero') == 'zero nine'


def test_already_sorted_all_digits():
    s = ' '.join(WORDS)
    assert sort_numbers(s) == s


def test_reverse_sorted_all_digits():
    assert sort_numbers(' '.join(reversed(WORDS))) == ' '.join(WORDS)


def test_shuffled_all_digits():
    shuffled = 'five zero nine two seven one eight three six four'
    assert sort_numbers(shuffled) == ' '.join(WORDS)


def test_numeric_order_not_alphabetical():
    # alphabetical would put 'eight' first, numeric puts 'one' first
    assert sort_numbers('eight one') == 'one eight'


def test_numeric_order_four_vs_five_vs_nine():
    assert sort_numbers('nine five four') == 'four five nine'


def test_numeric_order_two_vs_three():
    assert sort_numbers('three two') == 'two three'


def test_numeric_order_six_seven_eight():
    assert sort_numbers('eight seven six') == 'six seven eight'


def test_duplicates_preserved():
    assert sort_numbers('three one three one') == 'one one three three'


def test_all_identical_words():
    assert sort_numbers('two two two') == 'two two two'


def test_duplicates_of_zero_and_nine():
    assert sort_numbers('nine zero nine zero') == 'zero zero nine nine'


def test_leading_space_ignored():
    assert sort_numbers(' three one') == 'one three'


def test_trailing_space_ignored():
    assert sort_numbers('three one ') == 'one three'


def test_leading_and_trailing_spaces_ignored():
    assert sort_numbers('   three one   ') == 'one three'


def test_multiple_spaces_between_words_collapsed():
    assert sort_numbers('three     one      two') == 'one two three'


def test_output_uses_single_spaces():
    result = sort_numbers('  nine   zero    five  ')
    assert '  ' not in result
    assert not result.startswith(' ')
    assert not result.endswith(' ')


def test_output_word_count_matches_input():
    s = 'five three nine one one zero'
    assert len(sort_numbers(s).split(' ')) == len(s.split())


def test_output_is_permutation_of_input():
    s = 'five three nine one one zero'
    assert sorted(sort_numbers(s).split(' ')) == sorted(s.split(' '))


def test_output_is_sorted_by_value():
    result = sort_numbers('seven two nine zero four four eight').split(' ')
    values = [WORDS.index(w) for w in result]
    assert values == sorted(values)


def test_idempotent():
    s = 'six two eight zero'
    once = sort_numbers(s)
    assert sort_numbers(once) == once


def test_matches_reference_implementation():
    s = 'four nine zero three three one eight'
    expected = ' '.join(sorted(s.split(), key=WORDS.index))
    assert sort_numbers(s) == expected


def test_long_input_all_words_repeated():
    tokens = WORDS * 100
    result = sort_numbers(' '.join(tokens)).split(' ')
    assert len(result) == 1000
    assert result == [w for w in WORDS for _ in range(100)]


def test_long_input_reversed_repeated():
    tokens = list(reversed(WORDS)) * 50
    result = sort_numbers(' '.join(tokens)).split(' ')
    assert result == [w for w in WORDS for _ in range(50)]


def test_returns_str_type():
    assert isinstance(sort_numbers('one two'), str)
    assert isinstance(sort_numbers(''), str)


def test_input_not_modified():
    s = 'three one two'
    sort_numbers(s)
    assert s == 'three one two'


def test_unknown_word_raises_key_error():
    with pytest.raises(KeyError):
        sort_numbers('one ten two')


def test_uppercase_word_raises_key_error():
    with pytest.raises(KeyError):
        sort_numbers('One two')


def test_digit_token_raises_key_error():
    with pytest.raises(KeyError):
        sort_numbers('1 2 3')


def test_misspelled_word_raises_key_error():
    with pytest.raises(KeyError):
        sort_numbers('one tow three')


def test_single_invalid_word_raises_key_error():
    with pytest.raises(KeyError):
        sort_numbers('eleven')


def test_tab_separator_not_supported():
    with pytest.raises(KeyError):
        sort_numbers('one\ttwo')


def test_newline_separator_not_supported():
    with pytest.raises(KeyError):
        sort_numbers('two\none')


def test_non_string_input_raises_attribute_error():
    with pytest.raises(AttributeError):
        sort_numbers(123)


def test_none_input_raises_attribute_error():
    with pytest.raises(AttributeError):
        sort_numbers(None)


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ('', ''),
        (' ', ''),
        ('zero', 'zero'),
        ('nine', 'nine'),
        ('one two', 'one two'),
        ('two one', 'one two'),
        ('three one five', 'one three five'),
        ('nine eight seven', 'seven eight nine'),
        ('five five five', 'five five five'),
        ('zero nine zero nine', 'zero zero nine nine'),
        ('  four   two  ', 'two four'),
        ('six four five', 'four five six'),
        ('one zero', 'zero one'),
        ('eight nine', 'eight nine'),
    ],
)
def test_parametrized_cases(numbers, expected):
    assert sort_numbers(numbers) == expected