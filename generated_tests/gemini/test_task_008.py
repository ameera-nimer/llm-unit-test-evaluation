from solutions.task_008 import sum_product


def test_sum_product_empty_list():
    assert sum_product([]) == (0, 1)


def test_sum_product_docstring_example():
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_sum_product_single_element():
    assert sum_product([5]) == (5, 5)


def test_sum_product_with_zero():
    assert sum_product([1, 2, 0, 4]) == (7, 0)


def test_sum_product_negative_numbers():
    assert sum_product([-1, -2, -3]) == (-6, -6)


def test_sum_product_mixed_numbers():
    assert sum_product([-2, 3, 4]) == (5, -24)