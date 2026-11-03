import math
import pytest
from solutions.task_021 import rescale_to_unit


def test_docstring_example():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == pytest.approx(
        [0.0, 0.25, 0.5, 0.75, 1.0]
    )


def test_two_elements_ascending():
    assert rescale_to_unit([0.0, 10.0]) == [0.0, 1.0]


def test_two_elements_descending():
    assert rescale_to_unit([10.0, 0.0]) == [1.0, 0.0]


def test_two_elements_arbitrary_values():
    assert rescale_to_unit([3.0, 7.0]) == [0.0, 1.0]


def test_already_unit_range():
    assert rescale_to_unit([0.0, 0.5, 1.0]) == pytest.approx([0.0, 0.5, 1.0])


def test_three_elements():
    assert rescale_to_unit([2.0, 4.0, 6.0]) == pytest.approx([0.0, 0.5, 1.0])


def test_unsorted_input_preserves_order():
    assert rescale_to_unit([3.0, 1.0, 5.0, 2.0, 4.0]) == pytest.approx(
        [0.5, 0.0, 1.0, 0.25, 0.75]
    )


def test_descending_input():
    assert rescale_to_unit([5.0, 4.0, 3.0, 2.0, 1.0]) == pytest.approx(
        [1.0, 0.75, 0.5, 0.25, 0.0]
    )


def test_minimum_maps_to_zero():
    result = rescale_to_unit([7.0, 3.0, 9.0, 5.0])
    assert min(result) == 0.0


def test_maximum_maps_to_one():
    result = rescale_to_unit([7.0, 3.0, 9.0, 5.0])
    assert max(result) == 1.0


def test_min_and_max_exact_for_awkward_values():
    result = rescale_to_unit([0.1, 0.7, 0.3, 0.9])
    assert min(result) == 0.0
    assert max(result) == 1.0


def test_all_values_within_unit_interval():
    result = rescale_to_unit([-8.5, 3.2, 100.0, 42.0, 0.0])
    assert all(0.0 <= v <= 1.0 for v in result)


def test_negative_numbers():
    assert rescale_to_unit([-3.0, -2.0, -1.0]) == pytest.approx([0.0, 0.5, 1.0])


def test_mixed_sign_numbers():
    assert rescale_to_unit([-1.0, 0.0, 1.0]) == pytest.approx([0.0, 0.5, 1.0])


def test_mixed_sign_asymmetric():
    assert rescale_to_unit([-2.0, 0.0, 6.0]) == pytest.approx([0.0, 0.25, 1.0])


def test_zero_in_input():
    assert rescale_to_unit([0.0, 5.0, 10.0]) == pytest.approx([0.0, 0.5, 1.0])


def test_duplicate_minimum_values():
    assert rescale_to_unit([1.0, 1.0, 3.0]) == pytest.approx([0.0, 0.0, 1.0])


def test_duplicate_maximum_values():
    assert rescale_to_unit([1.0, 3.0, 3.0]) == pytest.approx([0.0, 1.0, 1.0])


def test_duplicate_middle_values():
    assert rescale_to_unit([0.0, 5.0, 5.0, 10.0]) == pytest.approx([0.0, 0.5, 0.5, 1.0])


def test_integer_inputs():
    assert rescale_to_unit([1, 2, 3]) == pytest.approx([0.0, 0.5, 1.0])


def test_integer_inputs_two_elements():
    assert rescale_to_unit([5, 15]) == [0.0, 1.0]


def test_mixed_int_and_float_inputs():
    assert rescale_to_unit([1, 2.5, 4]) == pytest.approx([0.0, 0.5, 1.0])


def test_large_values():
    assert rescale_to_unit([1e12, 2e12, 3e12]) == pytest.approx([0.0, 0.5, 1.0])


def test_small_values():
    assert rescale_to_unit([1e-9, 2e-9, 3e-9]) == pytest.approx([0.0, 0.5, 1.0])


def test_large_offset_small_range():
    result = rescale_to_unit([1e6, 1e6 + 1.0, 1e6 + 2.0])
    assert result == pytest.approx([0.0, 0.5, 1.0])


def test_translation_invariance():
    data = [1.0, 4.0, 6.0, 9.0]
    shifted = [x + 100.0 for x in data]
    assert rescale_to_unit(shifted) == pytest.approx(rescale_to_unit(data))


def test_positive_scaling_invariance():
    data = [1.0, 4.0, 6.0, 9.0]
    scaled = [x * 7.0 for x in data]
    assert rescale_to_unit(scaled) == pytest.approx(rescale_to_unit(data))


def test_negative_scaling_reverses_result():
    data = [1.0, 4.0, 6.0, 9.0]
    negated = [-x for x in data]
    expected = [1.0 - v for v in rescale_to_unit(data)]
    assert rescale_to_unit(negated) == pytest.approx(expected)


def test_order_relationships_preserved():
    data = [3.0, 9.0, 1.0, 5.0, 7.0]
    result = rescale_to_unit(data)
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] < data[j]:
                assert result[i] < result[j]


def test_idempotent_on_rescaled_output():
    once = rescale_to_unit([2.0, 5.0, 11.0, 3.0])
    twice = rescale_to_unit(once)
    assert twice == pytest.approx(once)


def test_output_length_matches_input():
    data = [4.0, 8.0, 1.0, 9.0, 2.0, 6.0]
    assert len(rescale_to_unit(data)) == len(data)


def test_matches_reference_implementation():
    data = [12.5, -3.0, 7.25, 0.0, 30.0]
    lo, hi = min(data), max(data)
    expected = [(x - lo) / (hi - lo) for x in data]
    assert rescale_to_unit(data) == pytest.approx(expected)


def test_evenly_spaced_long_list():
    data = [float(i) for i in range(101)]
    result = rescale_to_unit(data)
    assert len(result) == 101
    assert result == pytest.approx([i / 100 for i in range(101)])


def test_long_list_bounds():
    data = [float((i * 37) % 1000) for i in range(1000)]
    result = rescale_to_unit(data)
    assert min(result) == 0.0
    assert max(result) == 1.0


def test_returns_list_type():
    assert isinstance(rescale_to_unit([1.0, 2.0]), list)


def test_returns_list_of_floats():
    assert all(isinstance(v, float) for v in rescale_to_unit([1, 2, 3]))


def test_input_list_not_modified():
    data = [3.0, 1.0, 2.0]
    original = list(data)
    rescale_to_unit(data)
    assert data == original


def test_returns_new_list_object():
    data = [1.0, 2.0]
    assert rescale_to_unit(data) is not data


def test_tuple_input_works():
    assert rescale_to_unit((1.0, 2.0, 3.0)) == pytest.approx([0.0, 0.5, 1.0])


def test_all_identical_elements_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([2.0, 2.0, 2.0])


def test_two_identical_elements_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([4.0, 4.0])


def test_single_element_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([5.0])


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        rescale_to_unit([])


def test_nan_input_does_not_produce_valid_range():
    result = rescale_to_unit([1.0, float("nan"), 3.0])
    assert any(math.isnan(v) for v in result) or len(result) == 3


def test_infinity_input_produces_nan():
    result = rescale_to_unit([1.0, float("inf")])
    assert any(math.isnan(v) for v in result)


def test_non_numeric_elements_raise_type_error():
    with pytest.raises(TypeError):
        rescale_to_unit([1.0, "a", 3.0])


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([0.0, 1.0], [0.0, 1.0]),
        ([1.0, 0.0], [1.0, 0.0]),
        ([0.0, 2.0], [0.0, 1.0]),
        ([1.0, 2.0, 3.0], [0.0, 0.5, 1.0]),
        ([3.0, 2.0, 1.0], [1.0, 0.5, 0.0]),
        ([1.0, 2.0, 3.0, 4.0, 5.0], [0.0, 0.25, 0.5, 0.75, 1.0]),
        ([-1.0, 0.0, 1.0], [0.0, 0.5, 1.0]),
        ([-10.0, 0.0, 10.0], [0.0, 0.5, 1.0]),
        ([10.0, 20.0, 15.0], [0.0, 1.0, 0.5]),
        ([0.0, 5.0, 5.0, 10.0], [0.0, 0.5, 0.5, 1.0]),
        ([100.0, 200.0], [0.0, 1.0]),
        ([2, 4, 8], [0.0, 1.0 / 3.0, 1.0]),
    ],
)
def test_parametrized_cases(numbers, expected):
    assert rescale_to_unit(numbers) == pytest.approx(expected)