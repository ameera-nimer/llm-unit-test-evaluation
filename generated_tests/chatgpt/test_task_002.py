
import pytest

from solutions.task_002 import truncate_number


def test_docstring_example():
    assert truncate_number(3.5) == pytest.approx(0.5)


def test_integer_part_with_zero_decimal():
    assert truncate_number(5.0) == pytest.approx(0.0)


def test_number_less_than_one():
    assert truncate_number(0.75) == pytest.approx(0.75)


def test_number_between_zero_and_one():
    assert truncate_number(0.25) == pytest.approx(0.25)


def test_integer_plus_small_decimal():
    assert truncate_number(4.1) == pytest.approx(0.1)


def test_integer_plus_large_decimal():
    assert truncate_number(7.9) == pytest.approx(0.9)


def test_number_with_multiple_decimal_digits():
    assert truncate_number(12.3456) == pytest.approx(0.3456)


def test_number_with_one_decimal_digit():
    assert truncate_number(8.2) == pytest.approx(0.2)


def test_number_with_two_decimal_digits():
    assert truncate_number(6.25) == pytest.approx(0.25)


def test_number_with_three_decimal_digits():
    assert truncate_number(9.125) == pytest.approx(0.125)


def test_zero():
    assert truncate_number(0.0) == pytest.approx(0.0)


def test_small_positive_number():
    assert truncate_number(0.001) == pytest.approx(0.001)


def test_very_small_positive_number():
    assert truncate_number(1e-10) == pytest.approx(1e-10)


def test_number_just_below_one():
    assert truncate_number(0.999) == pytest.approx(0.999)


def test_number_just_above_integer():
    assert truncate_number(5.001) == pytest.approx(0.001)


def test_large_positive_number():
    assert truncate_number(123456.75) == pytest.approx(0.75)


def test_large_integer():
    assert truncate_number(1000000.0) == pytest.approx(0.0)


def test_large_number_with_fractional_part():
    assert truncate_number(987654321.625) == pytest.approx(0.625)


def test_repeated_decimal_digits():
    assert truncate_number(2.7777) == pytest.approx(0.7777)


def test_fractional_part_with_trailing_zeros():
    assert truncate_number(3.1250) == pytest.approx(0.125)


def test_binary_floating_point_precision():
    assert truncate_number(1.3) == pytest.approx(0.3)


def test_fractional_part_close_to_zero():
    assert truncate_number(10.000001) == pytest.approx(0.000001)


def test_fractional_part_close_to_one():
    assert truncate_number(10.999999) == pytest.approx(0.999999)


def test_result_is_float():
    result = truncate_number(3.5)
    assert isinstance(result, float)


def test_result_is_non_negative_for_positive_input():
    result = truncate_number(7.35)
    assert result >= 0.0


def test_result_is_less_than_one_for_positive_input():
    result = truncate_number(7.85)
    assert result < 1.0


def test_result_matches_fractional_part():
    number = 14.625
    result = truncate_number(number)
    assert result == pytest.approx(number - int(number))


def test_integer_inputs_return_zero_fractional_part():
    assert truncate_number(7) == pytest.approx(0.0)


def test_multiple_calls_with_different_numbers():
    assert truncate_number(1.2) == pytest.approx(0.2)
    assert truncate_number(2.4) == pytest.approx(0.4)
    assert truncate_number(3.6) == pytest.approx(0.6)


@pytest.mark.parametrize(
    "number, expected",
    [
        (1.1, 0.1),
        (2.2, 0.2),
        (3.3, 0.3),
        (4.4, 0.4),
        (5.5, 0.5),
        (6.6, 0.6),
        (7.7, 0.7),
        (8.8, 0.8),
        (9.9, 0.9),
    ],
)
def test_various_single_decimal_values(number, expected):
    assert truncate_number(number) == pytest.approx(expected)


@pytest.mark.parametrize(
    "number",
    [1.0, 2.0, 10.0, 100.0, 1000.0],
)
def test_various_whole_numbers(number):
    assert truncate_number(number) == pytest.approx(0.0)


@pytest.mark.parametrize(
    "number",
    [0.1, 0.25, 0.5, 0.75, 0.99],
)
def test_various_numbers_between_zero_and_one(number):
    assert truncate_number(number) == pytest.approx(number)
