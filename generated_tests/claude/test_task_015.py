import pytest
from solutions.task_015 import string_sequence


def test_docstring_example_zero():
    assert string_sequence(0) == '0'


def test_docstring_example_five():
    assert string_sequence(5) == '0 1 2 3 4 5'


def test_one():
    assert string_sequence(1) == '0 1'


def test_two():
    assert string_sequence(2) == '0 1 2'


def test_ten():
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'


def test_single_digit_boundary_nine():
    assert string_sequence(9) == '0 1 2 3 4 5 6 7 8 9'


def test_two_digit_boundary_ten():
    assert string_sequence(10).split(' ')[-2:] == ['9', '10']


def test_three_digit_boundary_hundred():
    result = string_sequence(100)
    assert result.split(' ')[-2:] == ['99', '100']


def test_zero_returns_single_number_without_spaces():
    assert ' ' not in string_sequence(0)


def test_negative_one_returns_empty_string():
    assert string_sequence(-1) == ''


def test_negative_number_returns_empty_string():
    assert string_sequence(-5) == ''


def test_large_negative_returns_empty_string():
    assert string_sequence(-1000) == ''


def test_no_leading_space():
    assert not string_sequence(5).startswith(' ')


def test_no_trailing_space():
    assert not string_sequence(5).endswith(' ')


def test_no_double_spaces():
    assert '  ' not in string_sequence(50)


def test_starts_with_zero():
    assert string_sequence(7).startswith('0')


def test_ends_with_n():
    for n in [0, 1, 5, 10, 99, 100, 1000]:
        assert string_sequence(n).split(' ')[-1] == str(n)


def test_number_of_tokens_is_n_plus_one():
    for n in [0, 1, 2, 5, 10, 50, 100]:
        assert len(string_sequence(n).split(' ')) == n + 1


def test_space_count_equals_n():
    for n in [0, 1, 5, 20]:
        assert string_sequence(n).count(' ') == n


def test_tokens_are_consecutive_integers():
    tokens = string_sequence(25).split(' ')
    assert [int(t) for t in tokens] == list(range(26))


def test_matches_reference_implementation():
    for n in [0, 1, 3, 8, 15, 42]:
        assert string_sequence(n) == ' '.join(str(i) for i in range(n + 1))


def test_prefix_property():
    longer = string_sequence(10)
    shorter = string_sequence(5)
    assert longer.startswith(shorter)


def test_incremental_property():
    for n in range(0, 20):
        assert string_sequence(n + 1) == string_sequence(n) + ' ' + str(n + 1)


def test_no_leading_zeros_in_tokens():
    tokens = string_sequence(120).split(' ')
    assert all(t == str(int(t)) for t in tokens)


def test_only_digits_and_spaces():
    result = string_sequence(100)
    assert all(c.isdigit() or c == ' ' for c in result)


def test_large_n_token_count_and_ends():
    result = string_sequence(10000)
    tokens = result.split(' ')
    assert len(tokens) == 10001
    assert tokens[0] == '0'
    assert tokens[-1] == '10000'


def test_large_n_total_length():
    n = 999
    result = string_sequence(n)
    digits = 10 * 1 + 90 * 2 + 900 * 3
    spaces = n
    assert len(result) == digits + spaces


def test_returns_str_type():
    assert isinstance(string_sequence(0), str)
    assert isinstance(string_sequence(5), str)
    assert isinstance(string_sequence(-1), str)


def test_deterministic_repeated_calls():
    assert string_sequence(10) == string_sequence(10)


def test_bool_input_treated_as_int():
    assert string_sequence(True) == '0 1'
    assert string_sequence(False) == '0'


def test_float_input_raises_type_error():
    with pytest.raises(TypeError):
        string_sequence(3.5)


def test_string_input_raises_type_error():
    with pytest.raises(TypeError):
        string_sequence('5')


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        string_sequence(None)


@pytest.mark.parametrize(
    "n, expected",
    [
        (-10, ''),
        (-1, ''),
        (0, '0'),
        (1, '0 1'),
        (2, '0 1 2'),
        (3, '0 1 2 3'),
        (5, '0 1 2 3 4 5'),
        (9, '0 1 2 3 4 5 6 7 8 9'),
        (10, '0 1 2 3 4 5 6 7 8 9 10'),
        (12, '0 1 2 3 4 5 6 7 8 9 10 11 12'),
    ],
)
def test_parametrized_cases(n, expected):
    assert string_sequence(n) == expected