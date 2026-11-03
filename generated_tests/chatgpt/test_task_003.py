
import pytest

from solutions.task_003 import below_zero


def test_docstring_example_no_negative_balance():
    assert below_zero([1, 2, 3]) is False


def test_docstring_example_negative_balance():
    assert below_zero([1, 2, -4, 5]) is True


def test_empty_operations_list():
    assert below_zero([]) is False


def test_no_operations_below_zero():
    assert below_zero([5, -2, 3, -1]) is False


def test_single_positive_deposit():
    assert below_zero([10]) is False


def test_single_negative_withdrawal():
    assert below_zero([-1]) is True


def test_balance_exactly_zero():
    assert below_zero([5, -5]) is False


def test_balance_drops_below_zero_after_reaching_zero():
    assert below_zero([5, -5, -1]) is True


def test_balance_never_negative_despite_withdrawals():
    assert below_zero([10, -3, -4, -3]) is False


def test_balance_negative_on_first_operation():
    assert below_zero([-10, 20]) is True


def test_balance_negative_after_multiple_operations():
    assert below_zero([5, 3, -2, -4, -3]) is True


def test_later_deposit_does_not_undo_negative_balance():
    assert below_zero([2, -5, 10]) is True


def test_zero_operations_only():
    assert below_zero([0, 0, 0]) is False


def test_zero_operations_before_negative_withdrawal():
    assert below_zero([0, 0, -1]) is True


def test_negative_operation_after_large_deposit():
    assert below_zero([100, -50, -49]) is False


def test_balance_drops_below_zero_by_one_unit():
    assert below_zero([3, -4]) is True


def test_large_positive_and_negative_operations():
    assert below_zero([1000000, -999999]) is False


def test_large_withdrawal_exceeds_deposit():
    assert below_zero([1000000, -1000001]) is True


def test_multiple_deposits_and_withdrawals():
    assert below_zero([10, 20, -5, -10, 3, -18]) is False


def test_negative_balance_occurs_in_middle():
    assert below_zero([10, -3, -8, 20]) is True


def test_negative_balance_occurs_at_last_operation():
    assert below_zero([5, -2, -2, -2]) is True


def test_all_positive_operations():
    assert below_zero([1, 2, 3, 4, 5]) is False


def test_all_negative_operations():
    assert below_zero([-1, -2, -3]) is True


def test_alternating_deposits_and_withdrawals():
    assert below_zero([5, -3, 4, -2, 1, -4]) is False


def test_balance_returns_to_zero_multiple_times():
    assert below_zero([5, -5, 3, -3, 2, -2]) is False


def test_negative_balance_after_returning_to_zero():
    assert below_zero([5, -5, 2, -3]) is True


def test_withdrawal_equal_to_current_balance():
    assert below_zero([7, -7]) is False


def test_withdrawal_one_greater_than_current_balance():
    assert below_zero([7, -8]) is True


def test_balance_never_negative_with_zero_and_positive_operations():
    assert below_zero([0, 5, 0, 3, 0]) is False


def test_function_returns_boolean():
    result = below_zero([1, -2])
    assert isinstance(result, bool)


@pytest.mark.parametrize(
    "operations, expected",
    [
        ([], False),
        ([1], False),
        ([-1], True),
        ([1, -1], False),
        ([1, -2], True),
        ([2, -1, -1], False),
        ([2, -1, -2], True),
        ([10, -5, -5], False),
        ([10, -5, -6], True),
        ([0, 0, 0], False),
    ],
)
def test_various_balance_sequences(operations, expected):
    assert below_zero(operations) is expected
