
import pytest

from solutions.task_004 import mean_absolute_deviation


def test_docstring_example():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)


def test_single_element():
    assert mean_absolute_deviation([5.0]) == pytest.approx(0.0)


def test_all_elements_equal():
    assert mean_absolute_deviation([3.0, 3.0, 3.0, 3.0]) == pytest.approx(0.0)


def test_two_elements():
    assert mean_absolute_deviation([2.0, 6.0]) == pytest.approx(2.0)


def test_two_identical_elements():
    assert mean_absolute_deviation([4.0, 4.0]) == pytest.approx(0.0)


def test_symmetric_values_around_zero():
    assert mean_absolute_deviation([-2.0, 2.0]) == pytest.approx(2.0)


def test_positive_and_negative_values():
    assert mean_absolute_deviation([-1.0, 0.0, 1.0]) == pytest.approx(2.0 / 3.0)


def test_all_positive_integers():
    assert mean_absolute_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.2)


def test_all_negative_numbers():
    assert mean_absolute_deviation([-5.0, -4.0, -3.0, -2.0, -1.0]) == pytest.approx(1.2)


def test_values_with_zero():
    assert mean_absolute_deviation([0.0, 2.0, 4.0]) == pytest.approx(4.0 / 3.0)


def test_unsorted_values():
    assert mean_absolute_deviation([10.0, 1.0, 7.0, 2.0]) == pytest.approx(3.25)


def test_fractional_values():
    assert mean_absolute_deviation([1.5, 2.5, 3.5]) == pytest.approx(2.0 / 3.0)


def test_decimal_values():
    assert mean_absolute_deviation([0.1, 0.2, 0.3]) == pytest.approx(0.0 + 0.1 + 0.0, abs=1e-9)


def test_large_values():
    assert mean_absolute_deviation([1000.0, 2000.0, 3000.0]) == pytest.approx(2000.0 / 3.0)


def test_very_small_values():
    assert mean_absolute_deviation([0.0001, 0.0002, 0.0003]) == pytest.approx(0.0002 / 3.0)


def test_values_with_large_spread():
    assert mean_absolute_deviation([0.0, 100.0]) == pytest.approx(50.0)


def test_mean_is_not_an_element():
    assert mean_absolute_deviation([1.0, 2.0, 6.0]) == pytest.approx(20.0 / 9.0)


def test_repeated_values_with_one_outlier():
    assert mean_absolute_deviation([5.0, 5.0, 5.0, 20.0]) == pytest.approx(5.625)


def test_negative_and_positive_large_magnitudes():
    assert mean_absolute_deviation([-100.0, 100.0]) == pytest.approx(100.0)


def test_result_is_float():
    result = mean_absolute_deviation([1.0, 2.0, 3.0])
    assert isinstance(result, float)


def test_input_with_integer_values():
    assert mean_absolute_deviation([1, 2, 3]) == pytest.approx(2.0 / 3.0)


def test_input_with_mixed_integer_and_float_values():
    assert mean_absolute_deviation([1, 2.5, 4]) == pytest.approx(10.0 / 9.0)


def test_reordering_values_does_not_change_result():
    numbers1 = [1.0, 2.0, 3.0, 8.0]
    numbers2 = [8.0, 3.0, 1.0, 2.0]

    assert mean_absolute_deviation(numbers1) == pytest.approx(
        mean_absolute_deviation(numbers2)
    )


def test_translating_all_values_does_not_change_result():
    numbers = [1.0, 3.0, 5.0]
    shifted_numbers = [value + 10.0 for value in numbers]

    assert mean_absolute_deviation(shifted_numbers) == pytest.approx(
        mean_absolute_deviation(numbers)
    )


def test_scaling_all_values_scales_deviation():
    numbers = [1.0, 2.0, 5.0]
    scale = 3.0

    assert mean_absolute_deviation([x * scale for x in numbers]) == pytest.approx(
        scale * mean_absolute_deviation(numbers)
    )


def test_zero_values():
    assert mean_absolute_deviation([0.0, 0.0, 0.0]) == pytest.approx(0.0)


def test_two_values_with_fractional_difference():
    assert mean_absolute_deviation([1.25, 2.75]) == pytest.approx(0.75)


def test_symmetric_values_around_the_mean():
    assert mean_absolute_deviation([2.0, 4.0, 6.0]) == pytest.approx(4.0 / 3.0)


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1.0], 0.0),
        ([2.0, 4.0], 1.0),
        ([1.0, 2.0, 3.0], 2.0 / 3.0),
        ([1.0, 2.0, 3.0, 4.0], 1.0),
        ([10.0, 10.0, 10.0], 0.0),
        ([-1.0, 1.0], 1.0),
        ([0.0, 10.0, 20.0], 20.0 / 3.0),
    ],
)
def test_various_datasets(numbers, expected):
    assert mean_absolute_deviation(numbers) == pytest.approx(expected)


def test_empty_list_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])
