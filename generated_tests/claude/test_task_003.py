import pytest
from solutions.task_003 import below_zero


def test_docstring_example_no_negative_balance():
    assert below_zero([1, 2, 3]) is False


def test_docstring_example_goes_negative():
    assert below_zero([1, 2, -4, 5]) is True


def test_empty_list():
    assert below_zero([]) is False


def test_single_positive_operation():
    assert below_zero([5]) is False


def test_single_negative_operation():
    assert below_zero([-1]) is True


def test_single_zero_operation():
    assert below_zero([0]) is False


def test_all_zero_operations():
    assert below_zero([0, 0, 0, 0]) is False


def test_all_positive_operations():
    assert below_zero([10, 20, 30, 40]) is False


def test_all_negative_operations():
    assert below_zero([-1, -2, -3]) is True


def test_first_operation_negative():
    assert below_zero([-5, 10, 10]) is True


def test_last_operation_causes_negative():
    assert below_zero([5, 5, -11]) is True


def test_middle_operation_causes_negative():
    assert below_zero([3, -5, 10]) is True


def test_balance_reaches_exactly_zero_not_below():
    assert below_zero([5, -5]) is False


def test_balance_reaches_zero_multiple_times():
    assert below_zero([3, -3, 2, -2, 1, -1]) is False


def test_balance_goes_one_below_zero():
    assert below_zero([5, -6]) is True


def test_balance_one_above_zero_boundary():
    assert below_zero([5, -4]) is False


def test_goes_negative_then_recovers_still_true():
    assert below_zero([-1, 100]) is True


def test_goes_negative_then_positive_total_still_true():
    assert below_zero([1, -2, 10, 10]) is True


def test_final_balance_negative():
    assert below_zero([10, -5, -6]) is True


def test_final_balance_zero():
    assert below_zero([10, -5, -5]) is False


def test_net_positive_but_dips_negative_midway():
    assert below_zero([2, -3, 5, 5]) is True


def test_net_negative_but_never_dips_before_end():
    assert below_zero([10, -3, -3, -3]) is False


def test_large_positive_values():
    assert below_zero([10**9, 10**9, -10**9]) is False


def test_large_negative_value():
    assert below_zero([10**9, -(10**9) - 1]) is True


def test_zero_operations_interleaved():
    assert below_zero([0, 5, 0, -5, 0]) is False


def test_zero_operations_then_negative():
    assert below_zero([0, 0, -1]) is True


def test_long_list_never_negative():
    operations = [1, -1] * 1000
    assert below_zero(operations) is False


def test_long_list_negative_at_end():
    operations = [1, -1] * 1000 + [-1]
    assert below_zero(operations) is True


def test_long_list_negative_at_start():
    operations = [-1] + [1, -1] * 1000
    assert below_zero(operations) is True


def test_returns_bool_type():
    assert isinstance(below_zero([1, 2, 3]), bool)
    assert isinstance(below_zero([-1]), bool)
    assert isinstance(below_zero([]), bool)


def test_input_list_not_modified():
    operations = [1, -2, 3]
    original = list(operations)
    below_zero(operations)
    assert operations == original


def test_tuple_input_works():
    assert below_zero((1, -2)) is True
    assert below_zero((2, -1)) is False


@pytest.mark.parametrize(
    "operations, expected",
    [
        ([], False),
        ([0], False),
        ([1], False),
        ([-1], True),
        ([1, -1], False),
        ([1, -2], True),
        ([2, -1, -1], False),
        ([2, -1, -2], True),
        ([-1, 1], True),
        ([5, 5, -10], False),
        ([5, 5, -11], True),
        ([1, 2, 3, -6], False),
        ([1, 2, 3, -7], True),
    ],
)
def test_parametrized_cases(operations, expected):
    assert below_zero(operations) is expected