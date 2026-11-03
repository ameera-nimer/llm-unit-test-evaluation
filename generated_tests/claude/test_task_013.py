import math
import pytest
from solutions.task_013 import greatest_common_divisor


def test_docstring_example_coprime():
    assert greatest_common_divisor(3, 5) == 1


def test_docstring_example_common_factor():
    assert greatest_common_divisor(25, 15) == 5


def test_equal_numbers():
    assert greatest_common_divisor(7, 7) == 7


def test_one_divides_other_first_larger():
    assert greatest_common_divisor(10, 5) == 5


def test_one_divides_other_second_larger():
    assert greatest_common_divisor(5, 10) == 5


def test_first_larger_than_second():
    assert greatest_common_divisor(48, 18) == 6


def test_second_larger_than_first():
    assert greatest_common_divisor(18, 48) == 6


def test_gcd_with_one_first():
    assert greatest_common_divisor(1, 100) == 1


def test_gcd_with_one_second():
    assert greatest_common_divisor(100, 1) == 1


def test_both_ones():
    assert greatest_common_divisor(1, 1) == 1


def test_coprime_large_numbers():
    assert greatest_common_divisor(17, 31) == 1


def test_consecutive_integers_are_coprime():
    for n in range(1, 50):
        assert greatest_common_divisor(n, n + 1) == 1


def test_both_primes_distinct():
    assert greatest_common_divisor(13, 17) == 1


def test_same_prime():
    assert greatest_common_divisor(13, 13) == 13


def test_powers_of_two():
    assert greatest_common_divisor(64, 16) == 16
    assert greatest_common_divisor(16, 64) == 16


def test_powers_of_two_mixed():
    assert greatest_common_divisor(1024, 48) == 16


def test_multiples_of_common_factor():
    assert greatest_common_divisor(12 * 7, 12 * 11) == 12


def test_fibonacci_consecutive_worst_case():
    assert greatest_common_divisor(89, 55) == 1
    assert greatest_common_divisor(55, 89) == 1


def test_zero_second_argument_returns_first():
    assert greatest_common_divisor(5, 0) == 5


def test_zero_first_argument_returns_second():
    assert greatest_common_divisor(0, 5) == 5


def test_both_zero_returns_zero():
    assert greatest_common_divisor(0, 0) == 0


def test_zero_with_one():
    assert greatest_common_divisor(0, 1) == 1
    assert greatest_common_divisor(1, 0) == 1


def test_large_numbers():
    assert greatest_common_divisor(10**12, 10**9) == 10**9


def test_large_coprime_numbers():
    assert greatest_common_divisor(10**9 + 7, 10**9 + 9) == 1


def test_very_large_numbers_beyond_64_bit():
    a = 2**100
    b = 2**80 * 3
    assert greatest_common_divisor(a, b) == 2**80


def test_large_common_factor_product():
    g = 982451653
    assert greatest_common_divisor(g * 6, g * 15) == g * 3


def test_commutative():
    for a, b in [(12, 18), (100, 75), (17, 5), (0, 9), (81, 27)]:
        assert greatest_common_divisor(a, b) == greatest_common_divisor(b, a)


def test_gcd_with_self_is_self():
    for n in [1, 2, 3, 10, 97, 1000]:
        assert greatest_common_divisor(n, n) == n


def test_gcd_with_multiple_returns_smaller():
    for n in [1, 3, 7, 12]:
        for k in [1, 2, 5, 10]:
            assert greatest_common_divisor(n, n * k) == n


def test_scaling_property():
    a, b, k = 12, 18, 5
    assert greatest_common_divisor(a * k, b * k) == k * greatest_common_divisor(a, b)


def test_result_divides_both_inputs():
    for a, b in [(48, 18), (100, 75), (17, 5), (1000, 250), (36, 60)]:
        g = greatest_common_divisor(a, b)
        assert a % g == 0
        assert b % g == 0


def test_associativity_of_gcd():
    a, b, c = 24, 36, 60
    left = greatest_common_divisor(greatest_common_divisor(a, b), c)
    right = greatest_common_divisor(a, greatest_common_divisor(b, c))
    assert left == right == 12


def test_matches_math_gcd_for_positive_range():
    for a in range(1, 40):
        for b in range(1, 40):
            assert greatest_common_divisor(a, b) == math.gcd(a, b)


def test_matches_math_gcd_for_random_like_values():
    pairs = [(1071, 462), (270, 192), (123456, 7890), (2**20, 2**15 * 3), (999999, 333333)]
    for a, b in pairs:
        assert greatest_common_divisor(a, b) == math.gcd(a, b)


def test_negative_second_argument():
    # Python's modulo yields a result with the sign of the divisor
    assert abs(greatest_common_divisor(12, -8)) == 4


def test_negative_first_argument():
    assert abs(greatest_common_divisor(-12, 8)) == 4


def test_both_negative():
    assert abs(greatest_common_divisor(-12, -18)) == 6


def test_returns_int_type():
    assert isinstance(greatest_common_divisor(12, 18), int)
    assert isinstance(greatest_common_divisor(0, 0), int)


def test_result_positive_for_positive_inputs():
    for a, b in [(1, 1), (2, 3), (10, 15), (100, 1000)]:
        assert greatest_common_divisor(a, b) > 0


def test_non_numeric_input_raises_type_error():
    with pytest.raises(TypeError):
        greatest_common_divisor(10, "5")


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        greatest_common_divisor(10, None)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 5, 1),
        (25, 15, 5),
        (1, 1, 1),
        (2, 4, 2),
        (4, 2, 2),
        (12, 8, 4),
        (100, 10, 10),
        (17, 17, 17),
        (0, 7, 7),
        (7, 0, 7),
        (0, 0, 0),
        (35, 49, 7),
        (270, 192, 6),
        (1071, 462, 21),
        (2**10, 2**5, 2**5),
    ],
)
def test_parametrized_cases(a, b, expected):
    assert greatest_common_divisor(a, b) == expected