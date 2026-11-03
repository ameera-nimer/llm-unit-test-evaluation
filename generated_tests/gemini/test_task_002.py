import pytest
from solutions.task_002 import truncate_number


def test_truncate_number_docstring_example():
    assert truncate_number(3.5) == 0.5


def test_truncate_number_integer():
    assert truncate_number(5.0) == 0.0


def test_truncate_number_small_decimal():
    assert truncate_number(0.123) == pytest.approx(0.123)


def test_truncate_number_large_number():
    assert truncate_number(12345.6789) == pytest.approx(0.6789)


def test_truncate_number_just_above_integer():
    assert truncate_number(1.0001) == pytest.approx(0.0001)


def test_truncate_number_just_below_integer():
    assert truncate_number(1.9999) == pytest.approx(0.9999)