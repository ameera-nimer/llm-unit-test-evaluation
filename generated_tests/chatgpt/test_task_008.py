import pytest
from solutions.task_008 import sum_product


def test_empty_list():
    assert sum_product([]) == (0, 1)


def test_docstring_example():
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_single_positive_integer():
    assert sum_product([5]) == (5, 5)


def test_single_zero():
    assert sum_product([0]) == (0, 0)


def test_single_negative_integer():
    assert sum_product([-5]) == (-5, -5)


def test_all_positive_integers():
    assert sum_product([2, 3, 4]) == (9, 24)


def test_all_negative_integers():
    assert sum_product([-2, -3, -4]) == (-9, -24)


def test_mixed_positive_and_negative_integers():
    assert sum_product([-2, 3, -4]) == (-3, 24)


def test_list_containing_zero():
    assert sum_product([1, 2, 0, 4]) == (7, 0)


def test_multiple_zeros():
    assert sum_product([0, 0, 0]) == (0, 0)


def test_two_negative_integers():
    assert sum_product([-3, -4]) == (-7, 12)


def test_odd_number_of_negative_integers():
    assert sum_product([-1, -2, -3]) == (-6, -6)


def test_even_number_of_negative_integers():
    assert sum_product([-1, -2, -3, -4]) == (-10, 24)


def test_list_of_ones():
    assert sum_product([1, 1, 1, 1]) == (4, 1)


def test_list_of_negative_ones():
    assert sum_product([-1, -1, -1]) == (-3, -1)


def test_repeated_integers():
    assert sum_product([3, 3, 3]) == (9, 27)


def test_large_positive_integers():
    assert sum_product([1000, 2000, 3000]) == (6000, 6000000000)


def test_large_negative_integers():
    assert sum_product([-100, -200]) == (-300, 20000)


def test_mixed_values_with_zero():
    assert sum_product([-5, 0, 5]) == (0, 0)


def test_sum_zero_but_nonzero_product():
    assert sum_product([-2, 2]) == (0, -4)


def test_product_one_with_mixed_values():
    assert sum_product([-1, -1, 1]) == (-1, 1)


def test_two_element_list():
    assert sum_product([7, 8]) == (15, 56)


def test_list_with_minimum_integer_values():
    assert sum_product([-1, 0, 1]) == (0, 0)


def test_order_does_not_change_result():
    assert sum_product([2, -3, 4]) == sum_product([4, 2, -3])


def test_result_is_tuple():
    result = sum_product([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_single_large_integer():
    assert sum_product([10**12]) == (10**12, 10**12)


def test_empty_list_identity_values():
    result = sum_product([])
    assert result[0] == 0
    assert result[1] == 1