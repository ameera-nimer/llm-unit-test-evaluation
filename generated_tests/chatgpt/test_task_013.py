import pytest
from solutions.task_013 import greatest_common_divisor


def test_coprime_numbers():
    assert greatest_common_divisor(3, 5) == 1


def test_docstring_example():
    assert greatest_common_divisor(25, 15) == 5


def test_equal_positive_numbers():
    assert greatest_common_divisor(12, 12) == 12


def test_one_number_is_one():
    assert greatest_common_divisor(1, 10) == 1


def test_gcd_with_one():
    assert greatest_common_divisor(1, 1) == 1


def test_first_number_is_zero():
    assert greatest_common_divisor(0, 5) == 5


def test_second_number_is_zero():
    assert greatest_common_divisor(7, 0) == 7


def test_both_numbers_are_zero():
    assert greatest_common_divisor(0, 0) == 0


def test_first_number_is_negative():
    assert greatest_common_divisor(-12, 8) == 4


def test_second_number_is_negative():
    assert greatest_common_divisor(12, -8) == 4


def test_both_numbers_are_negative():
    assert greatest_common_divisor(-12, -8) == 4


def test_negative_coprime_numbers():
    assert greatest_common_divisor(-7, -11) == 1


def test_first_number_is_multiple_of_second():
    assert greatest_common_divisor(24, 6) == 6


def test_second_number_is_multiple_of_first():
    assert greatest_common_divisor(6, 24) == 6


def test_gcd_of_large_numbers():
    assert greatest_common_divisor(123456, 7890) == 6


def test_gcd_of_large_coprime_numbers():
    assert greatest_common_divisor(1000003, 1000033) == 1


def test_gcd_of_large_multiples():
    assert greatest_common_divisor(1000000, 500000) == 500000


def test_consecutive_integers():
    assert greatest_common_divisor(100, 101) == 1


def test_numbers_with_common_factor():
    assert greatest_common_divisor(84, 126) == 42


def test_gcd_of_powers_of_two():
    assert greatest_common_divisor(64, 16) == 16


def test_gcd_of_even_and_odd_numbers():
    assert greatest_common_divisor(48, 15) == 3


def test_gcd_with_prime_numbers():
    assert greatest_common_divisor(13, 17) == 1


def test_gcd_of_same_prime_number():
    assert greatest_common_divisor(17, 17) == 17


def test_gcd_with_negative_multiple():
    assert greatest_common_divisor(-30, 10) == 10


def test_gcd_is_symmetric():
    assert greatest_common_divisor(54, 24) == greatest_common_divisor(24, 54)


def test_gcd_is_nonnegative_for_positive_inputs():
    assert greatest_common_divisor(18, 24) >= 0


def test_gcd_divides_both_inputs():
    a, b = 48, 18
    result = greatest_common_divisor(a, b)
    assert a % result == 0
    assert b % result == 0


def test_gcd_of_fibonacci_numbers():
    assert greatest_common_divisor(144, 89) == 1


def test_smallest_positive_integers():
    assert greatest_common_divisor(1, 2) == 1


def test_gcd_with_large_negative_numbers():
    assert greatest_common_divisor(-1000000, -250000) == 250000