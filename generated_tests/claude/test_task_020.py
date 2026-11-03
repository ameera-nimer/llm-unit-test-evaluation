import pytest
from solutions.task_020 import find_closest_elements


def test_docstring_example_close_pair():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)


def test_docstring_example_duplicate_pair():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)


def test_two_elements_sorted():
    assert find_closest_elements([1.0, 2.0]) == (1.0, 2.0)


def test_two_elements_unsorted_returns_ordered():
    assert find_closest_elements([2.0, 1.0]) == (1.0, 2.0)


def test_two_identical_elements():
    assert find_closest_elements([3.0, 3.0]) == (3.0, 3.0)


def test_three_elements_closest_first_two():
    assert find_closest_elements([1.0, 1.1, 5.0]) == (1.0, 1.1)


def test_three_elements_closest_last_two():
    assert find_closest_elements([1.0, 5.0, 5.2]) == (5.0, 5.2)


def test_three_elements_closest_first_and_last():
    assert find_closest_elements([1.0, 10.0, 1.5]) == (1.0, 1.5)


def test_result_is_ordered_smaller_first():
    a, b = find_closest_elements([9.0, 3.0, 8.5, 1.0])
    assert a <= b
    assert (a, b) == (8.5, 9.0)


def test_unsorted_input():
    assert find_closest_elements([10.0, 1.0, 7.0, 1.2, 4.0]) == (1.0, 1.2)


def test_sorted_ascending_input():
    assert find_closest_elements([1.0, 3.0, 6.0, 6.5, 10.0]) == (6.0, 6.5)


def test_sorted_descending_input():
    assert find_closest_elements([10.0, 6.5, 6.0, 3.0, 1.0]) == (6.0, 6.5)


def test_closest_pair_not_adjacent_in_input():
    assert find_closest_elements([5.0, 100.0, 200.0, 5.01]) == (5.0, 5.01)


def test_negative_numbers():
    assert find_closest_elements([-10.0, -5.0, -4.8, -1.0]) == (-5.0, -4.8)


def test_all_negative_numbers_ordered():
    assert find_closest_elements([-3.0, -1.0]) == (-3.0, -1.0)


def test_mixed_sign_numbers():
    assert find_closest_elements([-5.0, -0.1, 0.2, 5.0]) == (-0.1, 0.2)


def test_pair_straddling_zero():
    assert find_closest_elements([-0.5, 0.5, 10.0]) == (-0.5, 0.5)


def test_zeros():
    assert find_closest_elements([0.0, 0.0, 5.0]) == (0.0, 0.0)


def test_duplicates_win_over_near_values():
    assert find_closest_elements([1.0, 1.001, 7.0, 7.0]) == (7.0, 7.0)


def test_duplicate_negative_values():
    assert find_closest_elements([-4.0, 2.0, -4.0, 9.0]) == (-4.0, -4.0)


def test_all_identical_elements():
    assert find_closest_elements([2.5, 2.5, 2.5, 2.5]) == (2.5, 2.5)


def test_tie_returns_first_found_pair():
    # Pairs (1, 2) and (4, 5) both have distance 1; the first encountered wins
    assert find_closest_elements([1.0, 2.0, 4.0, 5.0]) == (1.0, 2.0)


def test_tie_first_pair_found_in_scan_order():
    assert find_closest_elements([4.0, 5.0, 1.0, 2.0]) == (4.0, 5.0)


def test_tie_with_equal_distances_three_values():
    assert find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)


def test_tie_resolved_by_strict_less_than():
    # Later pairs with equal distance must not replace the earlier result
    result = find_closest_elements([10.0, 11.0, 20.0, 21.0, 30.0, 31.0])
    assert result == (10.0, 11.0)


def test_integer_inputs():
    assert find_closest_elements([1, 5, 9, 5]) == (5, 5)


def test_integer_inputs_distinct():
    assert find_closest_elements([1, 10, 4, 20]) == (1, 4)


def test_mixed_int_and_float():
    assert find_closest_elements([1, 2.5, 2.6, 10]) == (2.5, 2.6)


def test_large_values():
    assert find_closest_elements([1e12, 2e12, 2e12 + 1.0, 5e12]) == (2e12, 2e12 + 1.0)


def test_very_small_differences():
    assert find_closest_elements([1.0, 1.0 + 1e-9, 2.0]) == (1.0, 1.0 + 1e-9)


def test_very_small_values():
    assert find_closest_elements([1e-9, 2e-9, 1.0]) == (1e-9, 2e-9)


def test_closest_pair_distance_is_minimal():
    numbers = [8.0, 1.5, 4.0, 1.9, 6.5, 12.0]
    a, b = find_closest_elements(numbers)
    best = min(
        abs(x - y)
        for i, x in enumerate(numbers)
        for j, y in enumerate(numbers)
        if i != j
    )
    assert abs(a - b) == pytest.approx(best)


def test_result_elements_come_from_input():
    numbers = [8.0, 1.5, 4.0, 1.9, 6.5, 12.0]
    a, b = find_closest_elements(numbers)
    assert a in numbers
    assert b in numbers


def test_duplicate_result_uses_two_occurrences():
    numbers = [3.0, 3.0, 8.0]
    assert find_closest_elements(numbers) == (3.0, 3.0)


def test_matches_reference_implementation():
    numbers = [7.3, 2.1, 9.9, 2.4, 5.5, 8.0, 7.0]
    best = None
    best_distance = None
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i != j:
                d = abs(x - y)
                if best_distance is None or d < best_distance:
                    best_distance = d
                    best = tuple(sorted([x, y]))
    assert find_closest_elements(numbers) == best


def test_long_list_with_one_obvious_close_pair():
    numbers = [float(i * 10) for i in range(200)]
    numbers.append(500.5)
    assert find_closest_elements(numbers) == (500.0, 500.5)


def test_long_list_evenly_spaced_returns_first_pair():
    numbers = [float(i) for i in range(100)]
    assert find_closest_elements(numbers) == (0.0, 1.0)


def test_returns_tuple_type():
    result = find_closest_elements([1.0, 2.0, 3.0])
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_input_list_not_modified():
    numbers = [5.0, 1.0, 3.0, 1.1]
    original = list(numbers)
    find_closest_elements(numbers)
    assert numbers == original


def test_tuple_input_works():
    assert find_closest_elements((1.0, 2.0, 2.1)) == (2.0, 2.1)


def test_single_element_returns_none():
    # No pair exists; the function never assigns closest_pair
    assert find_closest_elements([1.0]) is None


def test_empty_list_returns_none():
    assert find_closest_elements([]) is None


def test_non_numeric_elements_raise_type_error():
    with pytest.raises(TypeError):
        find_closest_elements([1.0, "a"])


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1.0, 2.0], (1.0, 2.0)),
        ([2.0, 1.0], (1.0, 2.0)),
        ([1.0, 1.0], (1.0, 1.0)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], (2.0, 2.2)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], (2.0, 2.0)),
        ([0.0, 10.0, 10.5], (10.0, 10.5)),
        ([-1.0, 0.0, 100.0], (-1.0, 0.0)),
        ([5.0, 4.0, 3.0], (4.0, 5.0)),
        ([100.0, 1.0, 50.0, 49.0], (49.0, 50.0)),
        ([-2.0, -2.5, 7.0], (-2.5, -2.0)),
        ([1, 3, 7, 7], (7, 7)),
        ([0.1, 0.2, 0.9], (0.1, 0.2)),
    ],
)
def test_parametrized_cases(numbers, expected):
    assert find_closest_elements(numbers) == expected