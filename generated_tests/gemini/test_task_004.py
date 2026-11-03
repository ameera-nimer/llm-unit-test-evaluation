import pytest
from solutions.task_004 import mean_absolute_deviation


def test_mean_absolute_deviation_docstring_example():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == pytest.approx(1.0)


def test_mean_absolute_deviation_identical_elements():
    assert mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_single_element():
    # Note: division by zero if len(numbers) is 0, but for single element len is 1, mean is the element, MAD is 0.0
    assert mean_absolute_deviation([42.0]) == pytest.approx(0.0)


def test_mean_absolute_deviation_negative_numbers():
    assert mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]) == pytest.approx(1.0)


def test_mean_absolute_deviation_mixed_numbers():
    # Numbers: [-2.0, 0.0, 2.0] -> mean = 0.0 -> abs diffs: [2.0, 0.0, 2.0] -> sum = 4.0 -> MAD = 4/3 = 1.3333333333333333
    assert mean_absolute_deviation([-2.0, 0.0, 2.0]) == pytest.approx(1.3333333333333333)


def test_mean_absolute_deviation_two_elements():
    # Numbers: [1.0, 3.0] -> mean = 2.0 -> abs diffs: [1.0, 1.0] -> MAD = 1.0
    assert mean_absolute_deviation([1.0, 3.0]) == pytest.approx(1.0)