from solutions.task_003 import below_zero


def test_below_zero_empty_list():
    assert below_zero([]) is False


def test_below_zero_all_positive():
    assert below_zero([1, 2, 3]) is False


def test_below_zero_drops_below_zero():
    assert below_zero([1, 2, -4, 5]) is True


def test_below_zero_reaches_exact_zero():
    assert below_zero([1, -1]) is False


def test_below_zero_immediate_drop():
    assert below_zero([-1, 5]) is True


def test_below_zero_drop_at_end():
    assert below_zero([5, -6]) is True


def test_below_zero_mixed_valid():
    assert below_zero([10, -5, 2, -3]) is False