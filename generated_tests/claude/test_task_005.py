import pytest
from solutions.task_005 import intersperse


def test_docstring_example_empty():
    assert intersperse([], 4) == []


def test_docstring_example_three_elements():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_single_element_no_delimiter_added():
    assert intersperse([5], 9) == [5]


def test_two_elements():
    assert intersperse([1, 2], 0) == [1, 0, 2]


def test_four_elements():
    assert intersperse([1, 2, 3, 4], 9) == [1, 9, 2, 9, 3, 9, 4]


def test_five_elements():
    assert intersperse([10, 20, 30, 40, 50], -1) == [10, -1, 20, -1, 30, -1, 40, -1, 50]


def test_result_length_formula():
    for n in range(1, 20):
        numbers = list(range(n))
        assert len(intersperse(numbers, -1)) == 2 * n - 1


def test_empty_list_length_zero():
    assert len(intersperse([], 7)) == 0


def test_delimiter_zero():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]


def test_negative_delimiter():
    assert intersperse([1, 2, 3], -5) == [1, -5, 2, -5, 3]


def test_negative_numbers_in_list():
    assert intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]


def test_delimiter_equals_element_values():
    assert intersperse([4, 4, 4], 4) == [4, 4, 4, 4, 4]


def test_all_elements_identical():
    assert intersperse([2, 2, 2], 3) == [2, 3, 2, 3, 2]


def test_list_with_zeros():
    assert intersperse([0, 0, 0], 1) == [0, 1, 0, 1, 0]


def test_large_values():
    assert intersperse([10**9, 10**10], 10**12) == [10**9, 10**12, 10**10]


def test_order_of_original_elements_preserved():
    numbers = [5, 3, 8, 1]
    result = intersperse(numbers, -1)
    assert result[::2] == numbers


def test_delimiters_at_odd_positions():
    result = intersperse([1, 2, 3, 4, 5], 99)
    assert result[1::2] == [99, 99, 99, 99]


def test_no_leading_delimiter():
    result = intersperse([1, 2, 3], 9)
    assert result[0] == 1


def test_no_trailing_delimiter():
    result = intersperse([1, 2, 3], 9)
    assert result[-1] == 3


def test_input_list_not_modified():
    numbers = [1, 2, 3]
    original = list(numbers)
    intersperse(numbers, 4)
    assert numbers == original


def test_returns_new_list_object():
    numbers = [1]
    result = intersperse(numbers, 4)
    assert result is not numbers
    assert result == numbers


def test_returns_list_type():
    assert isinstance(intersperse([1, 2], 3), list)
    assert isinstance(intersperse([], 3), list)


def test_empty_input_returns_new_list_each_call():
    first = intersperse([], 1)
    second = intersperse([], 1)
    assert first == second == []
    assert first is not second


def test_long_list():
    numbers = list(range(1000))
    result = intersperse(numbers, -1)
    assert len(result) == 1999
    assert result[::2] == numbers
    assert all(x == -1 for x in result[1::2])


def test_tuple_input_works():
    assert intersperse((1, 2, 3), 0) == [1, 0, 2, 0, 3]


def test_float_values_pass_through():
    assert intersperse([1.5, 2.5], 0.5) == [1.5, 0.5, 2.5]


@pytest.mark.parametrize(
    "numbers, delimeter, expected",
    [
        ([], 0, []),
        ([1], 0, [1]),
        ([1, 2], 0, [1, 0, 2]),
        ([1, 2, 3], 0, [1, 0, 2, 0, 3]),
        ([1, 2, 3], -1, [1, -1, 2, -1, 3]),
        ([7, 7], 7, [7, 7, 7]),
        ([0], 5, [0]),
        ([-1, 1], 100, [-1, 100, 1]),
        ([1, 2, 3, 4, 5, 6], 9, [1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6]),
    ],
)
def test_parametrized_cases(numbers, delimeter, expected):
    assert intersperse(numbers, delimeter) == expected