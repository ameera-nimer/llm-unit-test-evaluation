import pytest
from solutions.task_009 import rolling_max


def test_empty_list():
    assert rolling_max([]) == []


def test_docstring_example():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]


def test_single_element():
    assert rolling_max([5]) == [5]


def test_single_negative_element():
    assert rolling_max([-5]) == [-5]


def test_single_zero():
    assert rolling_max([0]) == [0]


def test_strictly_increasing_numbers():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_strictly_decreasing_numbers():
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]


def test_all_equal_numbers():
    assert rolling_max([3, 3, 3, 3]) == [3, 3, 3, 3]


def test_all_negative_numbers():
    assert rolling_max([-5, -2, -8, -3, -10]) == [-5, -2, -2, -2, -2]


def test_mixed_positive_and_negative_numbers():
    assert rolling_max([-3, 2, -5, 4, -1]) == [-3, 2, 2, 4, 4]


def test_list_containing_zero():
    assert rolling_max([-2, 0, -1, 3, 0]) == [-2, 0, 0, 3, 3]


def test_maximum_at_first_position():
    assert rolling_max([10, 2, 5, 1, 8]) == [10, 10, 10, 10, 10]


def test_maximum_at_last_position():
    assert rolling_max([1, 3, 2, 5, 10]) == [1, 3, 3, 5, 10]


def test_repeated_new_maximum():
    assert rolling_max([1, 5, 2, 7, 3, 9]) == [1, 5, 5, 7, 7, 9]


def test_repeated_maximum_values():
    assert rolling_max([2, 5, 5, 3, 5, 1]) == [2, 5, 5, 5, 5, 5]


def test_alternating_high_and_low_values():
    assert rolling_max([10, 1, 9, 2, 8, 3]) == [10, 10, 10, 10, 10, 10]


def test_negative_numbers_with_increasing_values():
    assert rolling_max([-10, -8, -6, -4, -2]) == [-10, -8, -6, -4, -2]


def test_negative_numbers_with_decreasing_values():
    assert rolling_max([-1, -3, -5, -7]) == [-1, -1, -1, -1]


def test_large_positive_integers():
    assert rolling_max([10**6, 10**9, 10**8, 10**12]) == [
        10**6, 10**9, 10**9, 10**12
    ]


def test_large_negative_integers():
    assert rolling_max([-10**9, -10**12, -10**6]) == [
        -10**9, -10**9, -10**6
    ]


def test_two_elements_increasing():
    assert rolling_max([1, 2]) == [1, 2]


def test_two_elements_decreasing():
    assert rolling_max([2, 1]) == [2, 2]


def test_two_equal_elements():
    assert rolling_max([4, 4]) == [4, 4]


def test_result_length_matches_input():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    assert len(rolling_max(numbers)) == len(numbers)


def test_result_preserves_running_maximum():
    numbers = [2, 7, 1, 8, 2, 8]
    result = rolling_max(numbers)
    assert result == [2, 7, 7, 8, 8, 8]


def test_result_is_a_list():
    result = rolling_max([1, 2, 3])
    assert isinstance(result, list)


def test_zeros_only():
    assert rolling_max([0, 0, 0, 0]) == [0, 0, 0, 0]


def test_maximum_occurs_multiple_times():
    assert rolling_max([1, 5, 2, 5, 3, 5]) == [1, 5, 5, 5, 5, 5]


def test_smallest_and_largest_integer_values():
    assert rolling_max([-10**18, 10**18, -10**18]) == [
        -10**18, 10**18, 10**18
    ]


def test_input_list_is_not_modified():
    numbers = [3, 1, 4, 2]
    original = numbers.copy()
    rolling_max(numbers)
    assert numbers == original