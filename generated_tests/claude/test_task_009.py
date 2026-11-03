import pytest
from solutions.task_009 import rolling_max


def test_docstring_example():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]


def test_empty_list():
    assert rolling_max([]) == []


def test_single_element():
    assert rolling_max([5]) == [5]


def test_single_negative_element():
    assert rolling_max([-5]) == [-5]


def test_single_zero_element():
    assert rolling_max([0]) == [0]


def test_two_elements_increasing():
    assert rolling_max([1, 2]) == [1, 2]


def test_two_elements_decreasing():
    assert rolling_max([2, 1]) == [2, 2]


def test_two_equal_elements():
    assert rolling_max([3, 3]) == [3, 3]


def test_strictly_increasing():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_strictly_decreasing():
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]


def test_all_identical_elements():
    assert rolling_max([7, 7, 7, 7]) == [7, 7, 7, 7]


def test_max_at_start():
    assert rolling_max([9, 1, 2, 3]) == [9, 9, 9, 9]


def test_max_at_end():
    assert rolling_max([1, 2, 3, 9]) == [1, 2, 3, 9]


def test_max_in_middle():
    assert rolling_max([1, 5, 2, 3]) == [1, 5, 5, 5]


def test_multiple_new_maxima():
    assert rolling_max([1, 3, 2, 5, 4, 7, 6]) == [1, 3, 3, 5, 5, 7, 7]


def test_all_negative_numbers():
    assert rolling_max([-5, -3, -4, -1, -2]) == [-5, -3, -3, -1, -1]


def test_all_negative_decreasing():
    assert rolling_max([-1, -2, -3]) == [-1, -1, -1]


def test_negative_then_positive():
    assert rolling_max([-3, -1, 2, 1]) == [-3, -1, 2, 2]


def test_positive_then_negative():
    assert rolling_max([3, -1, -5]) == [3, 3, 3]


def test_zeros_and_negatives():
    assert rolling_max([-1, 0, -2, 0]) == [-1, 0, 0, 0]


def test_all_zeros():
    assert rolling_max([0, 0, 0]) == [0, 0, 0]


def test_first_element_negative_is_not_treated_as_none():
    assert rolling_max([-10, -20]) == [-10, -10]


def test_first_element_zero_is_not_treated_as_none():
    assert rolling_max([0, -1, -2]) == [0, 0, 0]


def test_large_values():
    assert rolling_max([10**9, 10**12, 10**6]) == [10**9, 10**12, 10**12]


def test_output_length_matches_input():
    numbers = [4, 2, 8, 1, 9, 3]
    assert len(rolling_max(numbers)) == len(numbers)


def test_output_is_non_decreasing():
    result = rolling_max([5, 1, 7, 3, 9, 2, 8])
    assert all(result[i] <= result[i + 1] for i in range(len(result) - 1))


def test_each_output_at_least_corresponding_input():
    numbers = [5, 1, 7, 3, 9, 2, 8]
    result = rolling_max(numbers)
    assert all(r >= n for r, n in zip(result, numbers))


def test_last_output_equals_overall_max():
    numbers = [5, 1, 7, 3, 9, 2, 8]
    assert rolling_max(numbers)[-1] == max(numbers)


def test_first_output_equals_first_input():
    numbers = [4, 8, 1]
    assert rolling_max(numbers)[0] == numbers[0]


def test_matches_reference_implementation():
    numbers = [3, -2, 8, 8, 0, 11, -4, 11, 12]
    expected = [max(numbers[:i + 1]) for i in range(len(numbers))]
    assert rolling_max(numbers) == expected


def test_long_list_increasing():
    numbers = list(range(1000))
    assert rolling_max(numbers) == numbers


def test_long_list_decreasing():
    numbers = list(range(1000, 0, -1))
    assert rolling_max(numbers) == [1000] * 1000


def test_long_list_alternating():
    numbers = [1, 0] * 500
    assert rolling_max(numbers) == [1] * 1000


def test_input_list_not_modified():
    numbers = [3, 1, 2]
    original = list(numbers)
    rolling_max(numbers)
    assert numbers == original


def test_returns_new_list_object():
    numbers = [1, 2, 3]
    result = rolling_max(numbers)
    assert result is not numbers


def test_returns_list_type():
    assert isinstance(rolling_max([1, 2, 3]), list)
    assert isinstance(rolling_max([]), list)


def test_tuple_input_works():
    assert rolling_max((1, 3, 2)) == [1, 3, 3]


def test_float_values_pass_through():
    assert rolling_max([1.5, 0.5, 2.5, 2.0]) == [1.5, 1.5, 2.5, 2.5]


def test_mixed_int_and_float_values():
    assert rolling_max([1, 2.5, 2, 3]) == [1, 2.5, 2.5, 3]


def test_non_comparable_element_raises_type_error():
    with pytest.raises(TypeError):
        rolling_max([1, "a"])


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([], []),
        ([1], [1]),
        ([-1], [-1]),
        ([1, 2], [1, 2]),
        ([2, 1], [2, 2]),
        ([1, 1, 1], [1, 1, 1]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [3, 3, 3]),
        ([1, 3, 2, 4], [1, 3, 3, 4]),
        ([-3, -2, -5, -1], [-3, -2, -2, -1]),
        ([0, -1, 1, -2], [0, 0, 1, 1]),
        ([1, 2, 3, 2, 3, 4, 2], [1, 2, 3, 3, 3, 4, 4]),
    ],
)
def test_parametrized_cases(numbers, expected):
    assert rolling_max(numbers) == expected