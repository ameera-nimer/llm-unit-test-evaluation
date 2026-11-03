import math
import pytest
from solutions.task_008 import sum_product


def test_docstring_example_empty():
    assert sum_product([]) == (0, 1)


def test_docstring_example_four_elements():
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_single_positive_element():
    assert sum_product([5]) == (5, 5)


def test_single_negative_element():
    assert sum_product([-3]) == (-3, -3)


def test_single_zero_element():
    assert sum_product([0]) == (0, 0)


def test_single_one_element():
    assert sum_product([1]) == (1, 1)


def test_two_positive_elements():
    assert sum_product([2, 3]) == (5, 6)


def test_all_ones():
    assert sum_product([1, 1, 1, 1, 1]) == (5, 1)


def test_all_zeros():
    assert sum_product([0, 0, 0]) == (0, 0)


def test_contains_zero_product_is_zero():
    assert sum_product([1, 2, 0, 4]) == (7, 0)


def test_zero_at_start():
    assert sum_product([0, 5, 6]) == (11, 0)


def test_zero_at_end():
    assert sum_product([5, 6, 0]) == (11, 0)


def test_all_negative_even_count():
    assert sum_product([-1, -2, -3, -4]) == (-10, 24)


def test_all_negative_odd_count():
    assert sum_product([-1, -2, -3]) == (-6, -6)


def test_mixed_signs_negative_product():
    assert sum_product([2, -3, 4]) == (3, -24)


def test_mixed_signs_positive_product():
    assert sum_product([-2, -3, 4]) == (-1, 24)


def test_sum_cancels_to_zero():
    assert sum_product([5, -5]) == (0, -25)


def test_symmetric_values_sum_zero():
    assert sum_product([-2, -1, 1, 2]) == (0, 4)


def test_identical_elements():
    assert sum_product([3, 3, 3]) == (9, 27)


def test_with_one_and_minus_one():
    assert sum_product([1, -1, 1, -1]) == (0, 1)


def test_large_values():
    assert sum_product([10**6, 10**6]) == (2 * 10**6, 10**12)


def test_large_product_exceeds_64_bit():
    numbers = [10**10] * 5
    assert sum_product(numbers) == (5 * 10**10, 10**50)


def test_factorial_product():
    numbers = list(range(1, 11))