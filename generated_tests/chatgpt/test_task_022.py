import pytest
from solutions.task_022 import filter_integers


def test_docstring_example_with_mixed_values():
    assert filter_integers(["a", 3.14, 5]) == [5]


def test_docstring_example_with_various_types():
    assert filter_integers([1, 2, 3, "abc", {}, []]) == [1, 2, 3]


def test_empty_list():
    assert filter_integers([]) == []


def test_all_integers():
    assert filter_integers([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_no_integers():
    assert filter_integers(["hello", 2.5, None, {}, []]) == []


def test_negative_integers():
    assert filter_integers([-1, -5, 0, 3]) == [-1, -5, 0, 3]


def test_zero_is_integer():
    assert filter_integers([0, "0", 0.0]) == [0]


def test_boolean_values_are_integers():
    assert filter_integers([True, False, 1, 0]) == [True, False, 1, 0]


def test_floats_are_excluded():
    assert filter_integers([1.0, 2.5, -3.7, 4]) == [4]


def test_numeric_strings_are_excluded():
    assert filter_integers(["1", "2", "-3", 4]) == [4]


def test_mixed_nested_collections():
    values = [1, [2, 3], {"x": 4}, (5, 6), 7]
    assert filter_integers(values) == [1, 7]


def test_duplicate_integers_are_preserved():
    assert filter_integers([2, "a", 2, 3, 2]) == [2, 2, 3, 2]


def test_large_integers():
    assert filter_integers([10**100, "text", -(10**100)]) == [
        10**100, -(10**100)
    ]


def test_integer_subclasses_are_included():
    class CustomInt(int):
        pass

    assert filter_integers([CustomInt(7), "7", 8]) == [7, 8]


def test_boolean_values_mixed_with_other_types():
    assert filter_integers(["True", True, 3.0, False, None]) == [True, False]


def test_preserves_original_order():
    assert filter_integers([5, "x", -2, 3.5, 0, None]) == [5, -2, 0]


def test_returns_empty_list_for_only_booleans_and_non_integers():
    assert filter_integers([True, False, "hello", 1.5]) == [True, False]


def test_result_contains_only_integer_instances():
    result = filter_integers([1, "a", 2.5, 3, None])
    assert all(isinstance(value, int) for value in result)


def test_result_is_a_list():
    assert isinstance(filter_integers([1, "a", 2]), list)