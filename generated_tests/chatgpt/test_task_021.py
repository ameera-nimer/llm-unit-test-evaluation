import pytest
from solutions.task_021 import rescale_to_unit


def test_docstring_example():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [
        0.0, 0.25, 0.5, 0.75, 1.0
    ]


def test_two_elements_ascending():
    assert rescale_to_unit([2.0, 4.0]) == [0.0, 1.0]


def test_two_elements_descending():
    assert rescale_to_unit([4.0, 2.0]) == [1.0, 0.0]


def test_negative_numbers():
    assert rescale_to_unit([-10.0, -5.0, 0.0]) == [0.0, 0.5, 1.0]


def test_mixed_negative_and_positive_numbers():
    assert rescale_to_unit([-2.0, 0.0, 2.0]) == [0.0, 0.5, 1.0]


def test_unsorted_numbers():
    assert rescale_to_unit([5.0, 1.0, 3.0]) == [1.0, 0.0, 0.5]


def test_duplicate_values():
    assert rescale_to_unit([1.0, 2.0, 2.0, 3.0]) == [
        0.0, 0.5, 0.5, 1.0
    ]


def test_all_values_equal():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([5.0, 5.0, 5.0])


def test_zero_and_positive_numbers():
    assert rescale_to_unit([0.0, 5.0, 10.0]) == [0.0, 0.5, 1.0]


def test_zero_and_negative_numbers():
    assert rescale_to_unit([-10.0, -5.0, 0.0]) == [0.0, 0.5, 1.0]


def test_large_numbers():
    assert rescale_to_unit([1_000_000.0, 1_500_000.0, 2_000_000.0]) == [
        0.0, 0.5, 1.0
    ]


def test_small_decimal_values():
    result = rescale_to_unit([0.001, 0.002, 0.003])
    assert result == pytest.approx([0.0, 0.5, 1.0])


def test_result_preserves_input_order():
    result = rescale_to_unit([3.0, 1.0, 4.0, 2.0])
    assert result == [pytest.approx(2 / 3), 0.0, 1.0, pytest.approx(1 / 3)]


def test_minimum_maps_to_zero_and_maximum_maps_to_one():
    numbers = [8.0, 3.0, 12.0, 6.0]
    result = rescale_to_unit(numbers)
    assert result[numbers.index(min(numbers))] == 0.0
    assert result[numbers.index(max(numbers))] == 1.0


def test_all_results_are_within_unit_interval():
    result = rescale_to_unit([-3.0, 0.0, 2.0, 7.0])
    assert all(0.0 <= value <= 1.0 for value in result)


def test_integer_inputs():
    assert rescale_to_unit([0, 5, 10]) == [0.0, 0.5, 1.0]


def test_repeated_minimum_and_maximum():
    assert rescale_to_unit([1.0, 1.0, 3.0, 3.0]) == [
        0.0, 0.0, 1.0, 1.0
    ]


def test_result_length_matches_input_length():
    numbers = [4.0, 8.0, 2.0, 6.0]
    assert len(rescale_to_unit(numbers)) == len(numbers)


def test_result_is_a_list():
    assert isinstance(rescale_to_unit([1.0, 2.0]), list)