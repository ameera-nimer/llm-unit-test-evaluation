import pytest
from solutions.task_000 import has_close_elements


def test_docstring_example_no_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False


def test_docstring_example_with_close_elements():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) is True


def test_empty_list():
    assert has_close_elements([], 0.5) is False


def test_single_element():
    assert has_close_elements([1.0], 0.5) is False


def test_two_elements_close():
    assert has_close_elements([1.0, 1.1], 0.5) is True


def test_two_elements_far():
    assert has_close_elements([1.0, 5.0], 0.5) is False


def test_duplicate_elements_positive_threshold():
    assert has_close_elements([2.0, 2.0], 0.1) is True


def test_duplicate_elements_zero_threshold():
    # distance 0 is not strictly less than 0
    assert has_close_elements([2.0, 2.0], 0.0) is False


def test_boundary_distance_equals_threshold():
    # distance exactly equals threshold -> not strictly less
    assert has_close_elements([1.0, 2.0], 1.0) is False


def test_boundary_distance_just_below_threshold():
    assert has_close_elements([1.0, 2.0], 1.0001) is True


def test_boundary_distance_just_above_threshold():
    assert has_close_elements([1.0, 2.0], 0.9999) is False


def test_zero_threshold_distinct_elements():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0) is False


def test_negative_threshold():
    assert has_close_elements([1.0, 1.0, 2.0], -1.0) is False


def test_negative_numbers_close():
    assert has_close_elements([-1.0, -1.2, -5.0], 0.5) is True


def test_negative_numbers_far():
    assert has_close_elements([-10.0, -5.0, 0.0], 1.0) is False


def test_mixed_sign_numbers_close():
    assert has_close_elements([-0.1, 0.1], 0.5) is True


def test_mixed_sign_numbers_far():
    assert has_close_elements([-5.0, 5.0], 1.0) is False


def test_unsorted_list_close_pair_at_ends():
    assert has_close_elements([1.0, 10.0, 20.0, 1.05], 0.1) is True


def test_unsorted_list_no_close_pair():
    assert has_close_elements([10.0, 1.0, 20.0, 5.0], 1.0) is False


def test_close_pair_non_adjacent_in_input():
    assert has_close_elements([3.0, 10.0, 3.01, 20.0], 0.05) is True


def test_very_large_threshold():
    assert has_close_elements([1.0, 100.0, 1000.0], 10000.0) is True


def test_very_small_threshold_distinct_values():
    assert has_close_elements([1.0, 1.0001], 1e-9) is False


def test_very_small_distance_detected():
    assert has_close_elements([1.0, 1.0 + 1e-6], 1e-3) is True


def test_large_magnitude_numbers_far():
    assert has_close_elements([1e12, 2e12, 3e12], 1.0) is False


def test_large_magnitude_numbers_close():
    assert has_close_elements([1e12, 1e12 + 0.5], 1.0) is True


def test_integers_as_input():
    assert has_close_elements([1, 2, 3], 1.5) is True


def test_integers_boundary():
    assert has_close_elements([1, 3, 5], 2) is False


def test_all_identical_elements():
    assert has_close_elements([7.0, 7.0, 7.0, 7.0], 0.001) is True


def test_long_list_no_close_elements():
    numbers = [float(i * 10) for i in range(100)]
    assert has_close_elements(numbers, 5.0) is False


def test_long_list_with_one_close_pair():
    numbers = [float(i * 10) for i in range(100)]
    numbers.append(500.5)
    assert has_close_elements(numbers, 1.0) is True


def test_input_list_not_modified():
    numbers = [3.0, 1.0, 2.0]
    original = list(numbers)
    has_close_elements(numbers, 0.5)
    assert numbers == original


def test_returns_bool_type():
    assert isinstance(has_close_elements([1.0, 2.0], 0.5), bool)
    assert isinstance(has_close_elements([1.0, 1.1], 0.5), bool)


@pytest.mark.parametrize(
    "numbers, threshold, expected",
    [
        ([], 1.0, False),
        ([0.0], 1.0, False),
        ([0.0, 0.5], 1.0, True),
        ([0.0, 1.0], 1.0, False),
        ([0.0, 2.0, 4.0], 1.5, False),
        ([0.0, 2.0, 4.0], 2.5, True),
        ([-1.0, 1.0], 2.0, False),
        ([-1.0, 1.0], 2.1, True),
    ],
)
def test_parametrized_cases(numbers, threshold, expected):
    assert has_close_elements(numbers, threshold) is expected
