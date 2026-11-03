
import pytest

from solutions.task_005 import intersperse


def test_empty_list():
    assert intersperse([], 4) == []


def test_docstring_example():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_single_element_list():
    assert intersperse([5], 9) == [5]


def test_two_elements():
    assert intersperse([1, 2], 0) == [1, 0, 2]


def test_multiple_elements():
    assert intersperse([1, 2, 3, 4, 5], -1) == [1, -1, 2, -1, 3, -1, 4, -1, 5]


def test_zero_delimiter():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]


def test_negative_delimiter():
    assert intersperse([1, 2, 3], -5) == [1, -5, 2, -5, 3]


def test_negative_numbers():
    assert intersperse([-1, -2, -3], 9) == [-1, 9, -2, 9, -3]


def test_all_elements_are_equal():
    assert intersperse([7, 7, 7], 2) == [7, 2, 7, 2, 7]


def test_delimiter_equals_elements():
    assert intersperse([3, 3, 3], 3) == [3, 3, 3, 3, 3]


def test_delimiter_equals_first_element():
    assert intersperse([4, 2, 3], 4) == [4, 4, 2, 4, 3]


def test_delimiter_equals_last_element():
    assert intersperse([1, 2, 4], 4) == [1, 4, 2, 4, 4]


def test_delimiter_is_larger_than_all_elements():
    assert intersperse([1, 2, 3], 100) == [1, 100, 2, 100, 3]


def test_delimiter_is_smaller_than_all_elements():
    assert intersperse([10, 20, 30], -100) == [10, -100, 20, -100, 30]


def test_list_with_zero_elements():
    assert intersperse([0, 0, 0], 1) == [0, 1, 0, 1, 0]


def test_list_with_two_negative_elements():
    assert intersperse([-10, -20], -5) == [-10, -5, -20]


def test_large_integer_values():
    assert intersperse([1000000, 2000000], 999999) == [
        1000000,
        999999,
        2000000,
    ]


def test_single_zero_element():
    assert intersperse([0], 5) == [0]


def test_empty_list_with_zero_delimiter():
    assert intersperse([], 0) == []


def test_empty_list_with_negative_delimiter():
    assert intersperse([], -10) == []


def test_alternating_positive_and_negative_numbers():
    assert intersperse([1, -1, 2, -2], 0) == [1, 0, -1, 0, 2, 0, -2]


def test_original_order_is_preserved():
    numbers = [8, 3, 10, 1]
    result = intersperse(numbers, 99)

    assert result == [8, 99, 3, 99, 10, 99, 1]


def test_input_list_is_not_modified():
    numbers = [1, 2, 3]
    original = numbers.copy()

    intersperse(numbers, 0)

    assert numbers == original


def test_result_length_for_empty_list():
    assert len(intersperse([], 5)) == 0


def test_result_length_for_single_element():
    assert len(intersperse([10], 5)) == 1


def test_result_length_for_multiple_elements():
    numbers = [1, 2, 3, 4]
    assert len(intersperse(numbers, 0)) == 2 * len(numbers) - 1


def test_delimiter_appears_between_each_pair():
    numbers = [10, 20, 30, 40]
    delimiter = 99
    result = intersperse(numbers, delimiter)

    for index in range(1, len(result) - 1, 2):
        assert result[index] == delimiter


def test_first_and_last_elements_are_preserved():
    numbers = [11, 22, 33, 44]
    result = intersperse(numbers, 0)

    assert result[0] == numbers[0]
    assert result[-1] == numbers[-1]


def test_long_list():
    numbers = list(range(100))
    delimiter = -1
    expected = []

    for index, number in enumerate(numbers):
        expected.append(number)
        if index < len(numbers) - 1:
            expected.append(delimiter)

    assert intersperse(numbers, delimiter) == expected


@pytest.mark.parametrize(
    "numbers, delimiter, expected",
    [
        ([], 4, []),
        ([1], 4, [1]),
        ([1, 2], 4, [1, 4, 2]),
        ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
        ([5, 6, 7, 8], 0, [5, 0, 6, 0, 7, 0, 8]),
        ([-1, -2], -3, [-1, -3, -2]),
        ([0, 0], 0, [0, 0, 0]),
    ],
)
def test_various_inputs(numbers, delimiter, expected):
    assert intersperse(numbers, delimiter) == expected


def test_result_is_a_list():
    assert isinstance(intersperse([1, 2, 3], 0), list)


def test_original_elements_appear_at_even_indices():
    numbers = [7, 2, 9, 4]
    result = intersperse(numbers, -1)

    assert result[::2] == numbers


def test_delimiters_appear_at_odd_indices():
    numbers = [7, 2, 9, 4]
    delimiter = -1
    result = intersperse(numbers, delimiter)

    assert result[1::2] == [delimiter] * (len(numbers) - 1)
