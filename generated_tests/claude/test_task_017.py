import pytest
from solutions.task_017 import parse_music


def test_docstring_example():
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]


def test_empty_string():
    assert parse_music('') == []


def test_only_spaces():
    assert parse_music('     ') == []


def test_single_whole_note():
    assert parse_music('o') == [4]


def test_single_half_note():
    assert parse_music('o|') == [2]


def test_single_quarter_note():
    assert parse_music('.|') == [1]


def test_two_notes():
    assert parse_music('o o|') == [4, 2]


def test_three_different_notes():
    assert parse_music('o o| .|') == [4, 2, 1]


def test_three_different_notes_reversed():
    assert parse_music('.| o| o') == [1, 2, 4]


def test_all_whole_notes():
    assert parse_music('o o o o') == [4, 4, 4, 4]


def test_all_half_notes():
    assert parse_music('o| o| o|') == [2, 2, 2]


def test_all_quarter_notes():
    assert parse_music('.| .| .| .|') == [1, 1, 1, 1]


def test_alternating_notes():
    assert parse_music('o .| o .| o') == [4, 1, 4, 1, 4]


def test_leading_space_ignored():
    assert parse_music(' o o|') == [4, 2]


def test_trailing_space_ignored():
    assert parse_music('o o| ') == [4, 2]


def test_leading_and_trailing_spaces_ignored():
    assert parse_music('   o   .|   ') == [4, 1]


def test_multiple_spaces_between_notes():
    assert parse_music('o     o|     .|') == [4, 2, 1]


def test_output_length_matches_token_count():
    s = 'o o| .| o .| o|'
    assert len(parse_music(s)) == len(s.split())


def test_order_preserved():
    assert parse_music('.| o o| .| o') == [1, 4, 2, 1, 4]


def test_total_beats_sum():
    assert sum(parse_music('o o| .| .|')) == 8


def test_all_values_in_valid_set():
    result = parse_music('o o| .| o| .| o')
    assert set(result) <= {1, 2, 4}


def test_result_is_list_of_ints():
    result = parse_music('o o| .|')
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)


def test_long_input():
    s = ' '.join(['o', 'o|', '.|'] * 500)
    assert parse_music(s) == [4, 2, 1] * 500


def test_long_input_all_same_note():
    assert parse_music(' '.join(['o|'] * 1000)) == [2] * 1000


def test_matches_reference_implementation():
    mapping = {'o': 4, 'o|': 2, '.|': 1}
    s = 'o| .| .| o o| o .| o|'
    assert parse_music(s) == [mapping[t] for t in s.split()]


def test_input_not_modified():
    s = 'o o| .|'
    parse_music(s)
    assert s == 'o o| .|'


def test_unknown_note_raises_key_error():
    with pytest.raises(KeyError):
        parse_music('o x .|')


def test_uppercase_note_raises_key_error():
    with pytest.raises(KeyError):
        parse_music('O')


def test_malformed_note_raises_key_error():
    with pytest.raises(KeyError):
        parse_music('o||')


def test_reversed_quarter_note_raises_key_error():
    with pytest.raises(KeyError):
        parse_music('|.')


def test_notes_without_separator_raise_key_error():
    with pytest.raises(KeyError):
        parse_music('oo|')


def test_tab_separator_not_supported():
    with pytest.raises(KeyError):
        parse_music('o\to|')


def test_newline_separator_not_supported():
    with pytest.raises(KeyError):
        parse_music('o\no|')


def test_digit_token_raises_key_error():
    with pytest.raises(KeyError):
        parse_music('4')


def test_non_string_input_raises_attribute_error():
    with pytest.raises(AttributeError):
        parse_music(123)


def test_none_input_raises_attribute_error():
    with pytest.raises(AttributeError):
        parse_music(None)


@pytest.mark.parametrize(
    "music_string, expected",
    [
        ('', []),
        (' ', []),
        ('o', [4]),
        ('o|', [2]),
        ('.|', [1]),
        ('o o', [4, 4]),
        ('o| o|', [2, 2]),
        ('.| .|', [1, 1]),
        ('o o| .|', [4, 2, 1]),
        ('.| o| o', [1, 2, 4]),
        ('  o   o|  ', [4, 2]),
        ('o o| .| o| o| .| .| .| .| o o', [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]),
    ],
)
def test_parametrized_cases(music_string, expected):
    assert parse_music(music_string) == expected