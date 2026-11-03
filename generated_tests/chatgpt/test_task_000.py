import pytest

from solutions.task_000 import has_close_elements


def test_numbers_with_no_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False


def test_numbers_with_close_elements():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) is True


def test_empty_list():
    assert has_close_elements([], 1.0) is False


def test_single_element_list():
    assert has_close_elements([1.0], 1.0) is False


def test_two_identical_numbers():
    assert has_close_elements([2.5, 2.5], 0.1) is True


def test_duplicate_numbers_with_zero_threshold():
    assert has_close_elements([1.0, 1.0], 0.0) is False


def test_distance_less_than_threshold():
    assert has_close_elements([1.0, 1.4], 0.5) is True


def test_distance_equal_to_threshold():
    assert has_close_elements([1.0, 1.5], 0.5) is False


def test_distance_greater_than_threshold():
    assert has_close_elements([1.0, 1.6], 0.5) is False


def test_negative_numbers_close_together():
    assert has_close_elements([-2.0, -2.2], 0.3) is True


def test_positive_and_negative_numbers_close_together():
    assert has_close_elements([-0.1, 0.1], 0.3) is True


def test_positive_and_negative_numbers_far_apart():
    assert has_close_elements([-2.0, 2.0], 1.0) is False


def test_close_elements_at_end_of_list():
    assert has_close_elements([1.0, 5.0, 10.0, 10.1], 0.2) is True


def test_close_elements_at_beginning_of_list():
    assert has_close_elements([1.0, 1.1, 5.0, 10.0], 0.2) is True


def test_non_adjacent_elements_are_close():
    assert has_close_elements([1.0, 5.0, 1.2], 0.3) is True


def test_small_threshold():
    assert has_close_elements([1.0, 1.0001], 0.001) is True


def test_large_threshold():
    assert has_close_elements([1.0, 100.0], 100.0) is True


def test_zero_threshold_with_distinct_numbers():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0) is False


def test_negative_threshold():
    assert has_close_elements([1.0, 1.0], -1.0) is False


def test_floating_point_numbers():
    assert has_close_elements([0.1, 0.2], 0.11) is True


def test_numbers_with_large_magnitudes():
    assert has_close_elements([1e12, 1e12 + 0.5], 1.0) is True


def test_numbers_with_small_magnitudes():
    assert has_close_elements([1e-9, 2e-9], 2e-9) is True


def test_multiple_close_pairs():
    assert has_close_elements([1.0, 1.1, 5.0, 5.2], 0.3) is True


def test_all_numbers_far_apart():
    assert has_close_elements([-10.0, 0.0, 10.0, 20.0], 5.0) is False


def test_unsorted_numbers():
    assert has_close_elements([10.0, 1.0, 7.0, 1.2], 0.3) is True


def test_threshold_larger_than_all_pairwise_distances():
    assert has_close_elements([1.0, 2.0, 3.0], 10.0) is True


def test_threshold_just_below_pairwise_distance():
    assert has_close_elements([1.0, 2.0], 0.999) is False


def test_threshold_just_above_pairwise_distance():
    assert has_close_elements([1.0, 2.0], 1.001) is True


def test_integer_inputs():
    assert has_close_elements([1, 2, 2], 0.1) is True


def test_boolean_result_is_false_for_distinct_numbers_at_zero_threshold():
    result = has_close_elements([1.0, 2.0], 0.0)
    assert isinstance(result, bool)
    assert result is False
