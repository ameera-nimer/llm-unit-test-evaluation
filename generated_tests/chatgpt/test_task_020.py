import pytest
from solutions.task_020 import find_closest_elements


def test_docstring_example_with_decimal_values():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)


def test_docstring_example_with_duplicate_values():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)


def test_two_elements_in_ascending_order():
    assert find_closest_elements([1.0, 5.0]) == (1.0, 5.0)


def test_two_elements_in_descending_order():
    assert find_closest_elements([5.0, 1.0]) == (1.0, 5.0)


def test_closest_pair_at_beginning():
    assert find_closest_elements([1.0, 1.1, 5.0, 9.0]) == (1.0, 1.1)


def test_closest_pair_at_end():
    assert find_closest_elements([1.0, 5.0, 9.0, 9.2]) == (9.0, 9.2)


def test_closest_pair_in_middle():
    assert find_closest_elements([1.0, 5.0, 5.1, 10.0]) == (5.0, 5.1)


def test_negative_numbers():
    assert find_closest_elements([-10.0, -3.0, -3.2, 5.0]) == (-3.2, -3.0)


def test_mixed_positive_and_negative_numbers():
    assert find_closest_elements([-5.0, 0.0, 0.2, 8.0]) == (0.0, 0.2)


def test_identical_numbers():
    assert find_closest_elements([4.0, 4.0, 4.0]) == (4.0, 4.0)


def test_duplicate_values_with_other_numbers():
    assert find_closest_elements([1.0, 7.0, 3.0, 3.0, 10.0]) == (3.0, 3.0)


def test_integer_inputs():
    assert find_closest_elements([10, 3, 8, 4]) == (3, 4)


def test_small_decimal_difference():
    assert find_closest_elements([1.0, 1.001, 2.0, 3.0]) == (1.0, 1.001)


def test_large_numbers():
    assert find_closest_elements([1000000.0, 1000002.0, 1000001.5]) == (
        1000001.5, 1000002.0
    )


def test_closest_pair_returned_in_ascending_order():
    result = find_closest_elements([10.0, 2.0, 2.5, 7.0])
    assert result == (2.0, 2.5)
    assert result[0] <= result[1]


def test_input_order_does_not_change_unique_closest_pair():
    numbers = [10.0, 2.0, 8.0, 2.3]
    assert find_closest_elements(numbers) == (2.0, 2.3)
    assert find_closest_elements(list(reversed(numbers))) == (2.0, 2.3)


def test_closest_pair_among_evenly_spaced_numbers():
    assert find_closest_elements([0.0, 2.0, 4.0, 6.0]) == (0.0, 2.0)


def test_closest_pair_with_zero():
    assert find_closest_elements([-2.0, 0.0, 3.0, 0.5]) == (0.0, 0.5)


def test_tie_between_multiple_closest_pairs():
    result = find_closest_elements([1.0, 2.0, 4.0, 5.0])
    assert result in [(1.0, 2.0), (4.0, 5.0)]


def test_result_is_a_tuple():
    result = find_closest_elements([1.0, 1.5, 4.0])
    assert isinstance(result, tuple)
    assert len(result) == 2