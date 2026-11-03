import pytest
from solutions.task_024 import largest_divisor


def test_docstring_example():
    assert largest_divisor(15) == 5


def test_prime_number():
    assert largest_divisor(7) == 1


def test_another_prime_number():
    assert largest_divisor(13) == 1


def test_even_number():
    assert largest_divisor(10) == 5


def test_power_of_two():
    assert largest_divisor(16) == 8


def test_square_number():
    assert largest_divisor(25) == 5


def test_number_with_multiple_divisors():
    assert largest_divisor(24) == 12


def test_smallest_valid_input():
    assert largest_divisor(2) == 1


def test_number_three():
    assert largest_divisor(3) == 1


def test_number_four():
    assert largest_divisor(4) == 2


def test_number_six():
    assert largest_divisor(6) == 3


def test_number_nine():
    assert largest_divisor(9) == 3


def test_number_twelve():
    assert largest_divisor(12) == 6


def test_number_thirty():
    assert largest_divisor(30) == 15


def test_large_composite_number():
    assert largest_divisor(100) == 50


def test_large_prime_number():
    assert largest_divisor(101) == 1


def test_negative_input_returns_none():
    assert largest_divisor(-5) is None


def test_zero_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        largest_divisor(0)


def test_one_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        largest_divisor(1)