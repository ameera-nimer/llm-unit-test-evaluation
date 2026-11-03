import math
import pytest
from solutions.task_004 import mean_absolute_deviation


def test_docstring_example():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)


def test_simple_three_elements():
    # mean = 2, deviations = 1, 0, 1 -> 2/3
    assert mean_absolute_deviation([1.0, 2.0, 3.0]) == pytest.approx(2.0 / 3.0)


def test_two_elements():
    # mean = 5, deviations = 5, 5 -> 5
    assert mean_absolute_deviation([0.0, 10.0]) == pytest.approx(5.0)


def test_single_element_returns_zero():
    assert mean_absolute_deviation([5.0]) == 0.0


def test_all_identical_elements_returns_zero():
    assert mean_absolute_deviation([3.0, 3.0, 3.0, 3.0]) == pytest.approx(0.0)


def test_all_zeros():
    assert mean_absolute_deviation([0.0, 0.0, 0.0]) == 0.0


def test_two_identical_elements():
    assert mean_absolute_deviation([7.5, 7.5]) == pytest.approx(0.0)


def test_negative_numbers():
    # mean = -2, deviations = 1, 0, 1 -> 2/3
    assert mean_absolute_deviation([-1.0, -2.0, -3.0]) == pytest.approx(2.0 / 3.0)


def test_mixed_sign_numbers_symmetric():
    # mean = 0, deviations = 2, 1, 1, 2 -> 6/4
    assert mean_absolute_deviation([-2.0, -1.0, 1.0, 2.0]) == pytest.approx(1.5)


def test_mixed_sign_numbers_asymmetric():
    # mean = 0, deviations = 5, 3, 2 -> 10/3
    assert mean_absolute_deviation([-5.0, 3.0, 2.0]) == pytest.approx(10.0 / 3.0)


def test_integers_as_input():
    assert mean_absolute_deviation([1, 2, 3, 4]) == pytest.approx(1.0)


def test_unsorted_input_same_as_sorted():
    sorted_result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 10.0])
    unsorted_result = mean_absolute_deviation([10.0, 1.0, 4.0, 2.0, 3.0])
    assert sorted_result == pytest.approx(unsorted_result)


def test_known_value_with_outlier():
    # mean = 4, deviations = 3, 3, 3, 3, 6 ... use [1,1,1,1,10]: mean=2.8
    # deviations = 1.8*4 + 7.2 = 14.4 -> 14.4/5 = 2.88
    assert mean_absolute_deviation([1.0, 1.0, 1.0, 1.0, 10.0]) == pytest.approx(2.88)


def test_fractional_values():
    # mean = 0.5, deviations = 0.25, 0.25, 0.25, 0.25 -> 0.25
    assert mean_absolute_deviation([0.25, 0.75, 0.25, 0.75]) == pytest.approx(0.25)


def test_result_is_non_negative():
    for data in ([1.0, 2.0], [-5.0, 5.0], [0.1, 0.2, 0.3], [100.0, -100.0, 50.0]):
        assert mean_absolute_deviation(data) >= 0.0


def test_result_is_float():
    assert isinstance(mean_absolute_deviation([1.0, 2.0, 3.0]), float)
    assert isinstance(mean_absolute_deviation([5.0]), float)


def test_translation_invariance():
    data = [1.0, 4.0, 6.0, 9.0]
    shifted = [x + 100.0 for x in data]
    assert mean_absolute_deviation(shifted) == pytest.approx(
        mean_absolute_deviation(data)
    )


def test_scaling_property():
    data = [1.0, 4.0, 6.0, 9.0]
    scaled = [x * 3.0 for x in data]
    assert mean_absolute_deviation(scaled) == pytest.approx(
        3.0 * mean_absolute_deviation(data)
    )


def test_negation_invariance():
    data = [1.0, 4.0, 6.0, 9.0]
    negated = [-x for x in data]
    assert mean_absolute_deviation(negated) == pytest.approx(
        mean_absolute_deviation(data)
    )


def test_large_values():
    # mean = 2e9, deviations = 1e9, 0, 1e9 -> 2e9/3
    assert mean_absolute_deviation([1e9, 2e9, 3e9]) == pytest.approx(2e9 / 3.0)


def test_small_values():
    assert mean_absolute_deviation([1e-9, 2e-9, 3e-9]) == pytest.approx(
        2e-9 / 3.0, rel=1e-6
    )


def test_large_list():
    data = [float(i) for i in range(1, 1001)]
    # For 1..n with n even, MAD = n/4
    assert mean_absolute_deviation(data) == pytest.approx(250.0)


def test_input_list_not_modified():
    data = [3.0, 1.0, 2.0]
    original = list(data)
    mean_absolute_deviation(data)
    assert data == original


def test_tuple_input_works():
    assert mean_absolute_deviation((1.0, 2.0, 3.0, 4.0)) == pytest.approx(1.0)


def test_empty_list_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])


def test_nan_input_returns_nan():
    assert math.isnan(mean_absolute_deviation([1.0, float("nan"), 3.0]))


def test_infinity_input_returns_nan():
    assert math.isnan(mean_absolute_deviation([1.0, float("inf")]))


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1.0], 0.0),
        ([2.0, 2.0], 0.0),
        ([0.0, 2.0], 1.0),
        ([1.0, 3.0], 1.0),
        ([1.0, 2.0, 3.0, 4.0], 1.0),
        ([-1.0, 1.0], 1.0),
        ([0.0, 0.0, 6.0], 8.0 / 3.0),
        ([1.0, 2.0, 3.0], 2.0 / 3.0),
        ([10.0, 20.0, 30.0, 40.0], 10.0),
    ],
)
def test_parametrized_cases(numbers, expected):
    assert mean_absolute_deviation(numbers) == pytest.approx(expected)