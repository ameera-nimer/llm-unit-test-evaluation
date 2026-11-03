import pytest
from solutions.task_024 import largest_divisor


def test_docstring_example():
    assert largest_divisor(15) == 5


def test_two_is_smallest_valid_input():
    assert largest_divisor(2) == 1


def test_three_prime():
    assert largest_divisor(3) == 1


def test_four():
    assert largest_divisor(4) == 2


def test_six():
    assert largest_divisor(6) == 3


def test_eight():
    assert largest_divisor(8) == 4


def test_nine():
    assert largest_divisor(9) == 3


def test_ten():
    assert largest_divisor(10) == 5


def test_twelve():
    assert largest_divisor(12) == 6


def test_sixteen_power_of_two():
    assert largest_divisor(16) == 8


def test_twenty_five_square_of_prime():
    assert largest_divisor(25) == 5


def test_twenty_seven_power_of_three():
    assert largest_divisor(27) == 9


def test_thirty():
    assert largest_divisor(30) == 15


def test_forty_nine_square_of_prime():
    assert largest_divisor(49) == 7


def test_sixty_four():
    assert largest_divisor(64) == 32


def test_ninety_one_semiprime():
    assert largest_divisor(91) == 13


def test_hundred():
    assert largest_divisor(100) == 50


def test_hundred_twenty_one():
    assert largest_divisor(121) == 11


def test_thousand():
    assert largest_divisor(1000) == 500


def test_prime_returns_one():
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 97]:
        assert largest_divisor(p) == 1


def test_larger_prime_returns_one():
    assert largest_divisor(7919) == 1


def test_even_numbers_return_half():
    for n in range(2, 200, 2):
        assert largest_divisor(n) == n // 2


def test_powers_of_two_return_half():
    for k in range(1, 15):
        assert largest_divisor(2 ** k) == 2 ** (k - 1)


def test_powers_of_three():
    for k in range(1, 8):
        assert largest_divisor(3 ** k) == 3 ** (k - 1)


def test_prime_squared_returns_prime():
    for p in [2, 3, 5, 7, 11, 13]:
        assert largest_divisor(p * p) == p


def test_product_of_two_distinct_primes_returns_larger_prime():
    assert largest_divisor(3 * 5) == 5
    assert largest_divisor(5 * 7) == 7
    assert largest_divisor(11 * 13) == 13


def test_product_with_smallest_prime_factor():
    # n / smallest prime factor
    assert largest_divisor(3 * 5 * 7) == 35
    assert largest_divisor(7 * 11 * 13) == 143


def test_result_divides_n_evenly():
    for n in range(2, 300):
        assert n % largest_divisor(n) == 0


def test_result_is_smaller_than_n():
    for n in range(2, 300):
        assert largest_divisor(n) < n


def test_result_is_at_least_one():
    for n in range(2, 300):
        assert largest_divisor(n) >= 1


def test_no_larger_proper_divisor_exists():
    for n in range(2, 200):
        result = largest_divisor(n)
        for candidate in range(result + 1, n):
            assert n % candidate != 0


def test_matches_reference_implementation():
    def reference(n):
        for i in range(n - 1, 0, -1):
            if n % i == 0:
                return i

    for n in range(2, 500):
        assert largest_divisor(n) == reference(n)


def test_matches_smallest_prime_factor_formula():
    def smallest_prime_factor(n):
        d = 2
        while d * d <= n:
            if n % d == 0:
                return d
            d += 1
        return n

    for n in range(2, 300):
        assert largest_divisor(n) == n // smallest_prime_factor(n)


def test_large_even_number():
    assert largest_divisor(10 ** 6) == 500000


def test_large_prime_number():
    assert largest_divisor(999983) == 1


def test_large_odd_composite():
    assert largest_divisor(3 * 100003) == 100003


def test_returns_int_type():
    assert isinstance(largest_divisor(15), int)
    assert isinstance(largest_divisor(2), int)


def test_deterministic_repeated_calls():
    assert largest_divisor(36) == largest_divisor(36)


def test_one_raises_zero_division_error():
    # range(1) yields only 0, and 1 % 0 is invalid
    with pytest.raises(ZeroDivisionError):
        largest_divisor(1)


def test_zero_returns_none():
    # range(0) is empty, so the loop never runs
    assert largest_divisor(0) is None


def test_negative_one_returns_none():
    assert largest_divisor(-1) is None


def test_negative_number_returns_none():
    assert largest_divisor(-15) is None


def test_large_negative_number_returns_none():
    assert largest_divisor(-1000) is None


def test_true_behaves_like_one_and_raises():
    with pytest.raises(ZeroDivisionError):
        largest_divisor(True)


def test_false_behaves_like_zero_and_returns_none():
    assert largest_divisor(False) is None


def test_float_input_raises_type_error():
    with pytest.raises(TypeError):
        largest_divisor(15.0)


def test_string_input_raises_type_error():
    with pytest.raises(TypeError):
        largest_divisor('15')


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        largest_divisor(None)


def test_list_input_raises_type_error():
    with pytest.raises(TypeError):
        largest_divisor([15])


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 1),
        (6, 3),
        (7, 1),
        (8, 4),
        (9, 3),
        (10, 5),
        (12, 6),
        (15, 5),
        (16, 8),
        (17, 1),
        (18, 9),
        (20, 10),
        (21, 7),
        (25, 5),
        (28, 14),
        (35, 7),
        (49, 7),
        (97, 1),
        (100, 50),
    ],
)
def test_parametrized_cases(n, expected):
    assert largest_divisor(n) == expected


@pytest.mark.parametrize("n", [0, -1, -2, -10, -100])
def test_parametrized_non_positive_inputs_return_none(n):
    assert largest_divisor(n) is None