import pytest
from solutions.task_015 import string_sequence


def test_zero():
    assert string_sequence(0) == "0"


def test_docstring_example_five():
    assert string_sequence(5) == "0 1 2 3 4 5"


def test_one():
    assert string_sequence(1) == "0 1"


def test_two():
    assert string_sequence(2) == "0 1 2"


def test_negative_one():
    assert string_sequence(-1) == ""


def test_negative_number_less_than_negative_one():
    assert string_sequence(-5) == ""


def test_small_positive_number():
    assert string_sequence(3) == "0 1 2 3"


def test_ten():
    assert string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"


def test_sequence_starts_with_zero():
    result = string_sequence(8)
    assert result.split()[0] == "0"


def test_sequence_ends_with_n():
    n = 7
    result = string_sequence(n)
    assert result.split()[-1] == str(n)


def test_sequence_contains_all_numbers_in_order():
    assert string_sequence(4).split() == ["0", "1", "2", "3", "4"]


def test_sequence_length_for_zero():
    assert len(string_sequence(0).split()) == 1


def test_sequence_length_for_positive_number():
    n = 12
    assert len(string_sequence(n).split()) == n + 1


def test_numbers_are_space_delimited():
    assert string_sequence(3) == "0 1 2 3"


def test_no_leading_whitespace():
    result = string_sequence(5)
    assert not result.startswith(" ")


def test_no_trailing_whitespace():
    result = string_sequence(5)
    assert not result.endswith(" ")


def test_no_repeated_spaces():
    result = string_sequence(5)
    assert "  " not in result


def test_result_is_a_string():
    assert isinstance(string_sequence(5), str)


def test_large_number():
    n = 100
    result = string_sequence(n)
    assert result.split()[0] == "0"
    assert result.split()[-1] == "100"
    assert len(result.split()) == 101


def test_larger_number_sequence():
    n = 999
    result = string_sequence(n)
    numbers = result.split()
    assert numbers[0] == "0"
    assert numbers[-1] == "999"
    assert len(numbers) == 1000


def test_negative_input_returns_empty_string():
    assert string_sequence(-10) == ""


def test_consecutive_numbers():
    numbers = string_sequence(6).split()
    assert all(int(numbers[i + 1]) == int(numbers[i]) + 1 for i in range(len(numbers) - 1))


def test_sequence_matches_expected_range():
    n = 20
    expected = " ".join(str(i) for i in range(n + 1))
    assert string_sequence(n) == expected