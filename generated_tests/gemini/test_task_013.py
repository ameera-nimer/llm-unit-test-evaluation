from solutions.task_013 import greatest_common_divisor


def test_greatest_common_divisor_docstring_examples():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5


def test_greatest_common_divisor_one_number_is_zero():
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(7, 0) == 7


def test_greatest_common_divisor_both_zero():
    assert greatest_common_divisor(0, 0) == 0


def test_greatest_common_divisor_same_numbers():
    assert greatest_common_divisor(12, 12) == 12


def test_greatest_common_divisor_negative_numbers():
    assert greatest_common_divisor(-25, 15) == 5
    assert greatest_common_divisor(25, -15) == 5
    assert greatest_common_divisor(-25, -15) == 5


def test_greatest_common_divisor_coprime():
    assert greatest_common_divisor(17, 19) == 1