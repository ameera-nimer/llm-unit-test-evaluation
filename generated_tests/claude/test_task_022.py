import pytest
from solutions.task_022 import filter_integers


def test_docstring_example_mixed_types():
    assert filter_integers(['a', 3.14, 5]) == [5]


def test_docstring_example_with_containers():
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]


def test_empty_list():
    assert filter_integers([]) == []


def test_all_integers():
    assert filter_integers([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_no_integers():
    assert filter_integers(['a', 'b', 3.5, None, [], {}]) == []


def test_single_integer():
    assert filter_integers([7]) == [7]


def test_single_non_integer():
    assert filter_integers(['7']) == []


def test_zero_is_kept():
    assert filter_integers([0]) == [0]


def test_negative_integers_kept():
    assert filter_integers([-1, -100, 'x', -3]) == [-1, -100, -3]


def test_large_integers_kept():
    assert filter_integers([10**20, -(10**20), 1.5]) == [10**20, -(10**20)]


def test_strings_excluded():
    assert filter_integers(['1', '2', '3']) == []


def test_floats_excluded():
    assert filter_integers([1.0, 2.5, -3.0]) == []


def test_float_with_integer_value_excluded():
    assert filter_integers([1.0, 2, 3.0]) == [2]


def test_none_excluded():
    assert filter_integers([None, 1, None]) == [1]


def test_lists_excluded():
    assert filter_integers([[1], [2, 3], 4]) == [4]


def test_dicts_excluded():
    assert filter_integers([{1: 2}, 5, {}]) == [5]


def test_tuples_excluded():
    assert filter_integers([(1,), (), 9]) == [9]


def test_sets_excluded():
    assert filter_integers([{1, 2}, set(), 3]) == [3]


def test_complex_numbers_excluded():
    assert filter_integers([1 + 2j, 3, 0j]) == [3]


def test_bytes_excluded():
    assert filter_integers([b'1', b'', 2]) == [2]


def test_nan_and_inf_excluded():
    assert filter_integers([float('nan'), float('inf'), float('-inf'), 4]) == [4]


def test_booleans_are_treated_as_integers():
    # bool is a subclass of int in Python
    assert filter_integers([True, False, 2]) == [True, False, 2]


def test_boolean_values_equal_ints():
    assert filter_integers([True, False]) == [1, 0]


def test_order_preserved():
    assert filter_integers([5, 'a', 3, 'b', 9, 1]) == [5, 3, 9, 1]


def test_duplicates_preserved():
    assert filter_integers([1, 1, 'a', 2, 2, 1]) == [1, 1, 2, 2, 1]


def test_integers_at_start_and_end():
    assert filter_integers([1, 'a', 'b', 2]) == [1, 2]


def test_integers_only_in_middle():
    assert filter_integers(['a', 1, 2, 'b']) == [1, 2]


def test_custom_int_subclass_included():
    class MyInt(int):
        pass

    value = MyInt(5)
    result = filter_integers([value, 'x'])
    assert result == [5]
    assert result[0] is value


def test_custom_non_int_object_excluded():
    class Foo:
        pass

    assert filter_integers([Foo(), 1]) == [1]


def test_object_with_int_dunder_excluded():
    class Intlike:
        def __int__(self):
            return 3

    assert filter_integers([Intlike(), 3]) == [3]


def test_numeric_string_not_converted():
    assert filter_integers(['5', 5]) == [5]


def test_nested_integers_not_flattened():
    assert filter_integers([[1, 2], [3], 4]) == [4]


def test_result_is_list_type():
    assert isinstance(filter_integers([1, 'a']), list)
    assert isinstance(filter_integers([]), list)


def test_all_results_are_integers():
    result = filter_integers([1, 'a', 2.5, 3, None, [4]])
    assert all(isinstance(x, int) for x in result)


def test_result_is_subset_of_input():
    values = [1, 'a', 2.5, 3, None]
    result = filter_integers(values)
    assert all(x in values for x in result)


def test_input_list_not_modified():
    values = [1, 'a', 2, 3.5]
    original = list(values)
    filter_integers(values)
    assert values == original


def test_returns_new_list_object():
    values = [1, 2, 3]
    result = filter_integers(values)
    assert result == values
    assert result is not values


def test_empty_input_returns_new_list_each_call():
    first = filter_integers([])
    second = filter_integers([])
    assert first == second == []
    assert first is not second


def test_tuple_input_works():
    assert filter_integers((1, 'a', 2)) == [1, 2]


def test_generator_input_works():
    assert filter_integers(x for x in [1, 'a', 2]) == [1, 2]


def test_long_list_all_integers():
    values = list(range(10000))
    assert filter_integers(values) == values


def test_long_list_alternating_types():
    values = []
    for i in range(1000):
        values.append(i)
        values.append(str(i))
    assert filter_integers(values) == list(range(1000))


def test_long_list_no_integers():
    assert filter_integers(['x'] * 5000) == []


def test_non_iterable_input_raises_type_error():
    with pytest.raises(TypeError):
        filter_integers(5)


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        filter_integers(None)


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([1], [1]),
        (['a'], []),
        ([1, 2, 3], [1, 2, 3]),
        (['a', 3.14, 5], [5]),
        ([1, 2, 3, 'abc', {}, []], [1, 2, 3]),
        ([0, -1, 1], [0, -1, 1]),
        ([None, None], []),
        ([1.5, 2.5], []),
        ([[1], {2: 3}, (4,)], []),
        (['1', 1, '2', 2], [1, 2]),
        ([True, 5], [True, 5]),
        ([10**12, 'big'], [10**12]),
    ],
)
def test_parametrized_cases(values, expected):
    assert filter_integers(values) == expected