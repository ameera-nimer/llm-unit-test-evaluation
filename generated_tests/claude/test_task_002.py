import math
import pytest
from solutions.task_002 import truncate_number


def test_docstring_example():
    assert truncate_number(3.5) == 0.5


def test_simple_decimal():
    assert truncate_number(1.25) == pytest.approx(0.25)


def test_number_less_than_one():
    assert truncate_number(0.75) == pytest.approx(0.75)


def test_zero():
    assert truncate_number(0.0) == 0.0


def test_whole_number_returns_zero():
    assert truncate_number(5.0) == 0.0


def test_large_whole_number_returns_zero():
    assert truncate_number(1000000.0) == 0.0


def test_one():
    assert truncate_number(1.0) == 0.0


def test_just_above_integer():
    assert truncate_number(2.0001) == pytest.approx(0.0001, abs=1e-9)


def test_just_below_integer():
    assert truncate_number(2.9999) == pytest.approx(0.9999, abs=1e-9)


def test_point_five_values():
    assert truncate_number(0.5) == 0.5
    assert truncate_number(10.5) == 0.5
    assert truncate_number(100.5) == 0.5


def test_very_small_positive():
    assert truncate_number(1e-10) == pytest.approx(1e-10)


def test_very_small_fraction_on_large_integer():
    assert truncate_number(5.000001) == pytest.approx(0.000001, abs=1e-9)


def test_large_number_with_fraction():
    assert truncate_number(123456.789) == pytest.approx(0.789, abs=1e-6)


def test_very_large_float_has_no_fraction():
    assert truncate_number(1e16) == 0.0


def test_result_is_float():
    assert isinstance(truncate_number(3.5), float)
    assert isinstance(truncate_number(4.0), float)


def test_result_in_valid_range_for_positive_inputs():
    for value in [0.1, 0.5, 0.999, 1.0, 1.5, 2.75, 99.99, 12345.6789]:
        result = truncate_number(value)
        assert 0.0 <= result < 1.0


def test_integer_plus_decimal_reconstructs_number():
    for value in [0.25, 1.5, 7.125, 42.75, 100.375]:
        decimal = truncate_number(value)
        integer_part = math.floor(value)
        assert integer_part + decimal == pytest.approx(value)


def test_integer_input():
    result = truncate_number(7)
    assert result == 0
    assert result == pytest.approx(0.0)


def test_negative_number_uses_floor_modulo():
    # Python modulo with positive divisor yields a non-negative result
    assert truncate_number(-3.5) == pytest.approx(0.5)


def test_negative_whole_number():
    assert truncate_number(-2.0) == 0.0


def test_negative_small_fraction():
    assert truncate_number(-0.25) == pytest.approx(0.75)


def test_infinity_returns_nan():
    assert math.isnan(truncate_number(float("inf")))


def test_nan_returns_nan():
    assert math.isnan(truncate_number(float("nan")))


def test_idempotent_on_decimal_part():
    value = 8.375
    first = truncate_number(value)
    second = truncate_number(first)
    assert second == pytest.approx(first)


@pytest.mark.parametrize(
    "number, expected",
    [
        (0.0, 0.0),
        (0.5, 0.5),
        (1.0, 0.0),
        (1.5, 0.5),
        (2.25, 0.25),
        (3.75, 0.75),
        (10.125, 0.125),
        (99.0, 0.0),
        (0.0625, 0.0625),
        (5.875, 0.875),
    ],
)
def test_parametrized_cases(number, expected):
    assert truncate_number(number) == pytest.approx(expected)