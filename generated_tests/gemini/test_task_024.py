from solutions.task_024 import largest_divisor


def test_largest_divisor_docstring_example():
    assert largest_divisor(15) == 5


def test_largest_divisor_prime_number():
    assert largest_divisor(7) == 1


def test_largest_divisor_even_number():
    assert largest_divisor(10) == 5


def test_largest_divisor_power_of_two():
    assert largest_divisor(16) == 8


def test_largest_divisor_prime_square():
    assert largest_divisor(9) == 3