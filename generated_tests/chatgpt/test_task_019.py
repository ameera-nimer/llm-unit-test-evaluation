import pytest
from solutions.task_019 import sort_numbers


def test_docstring_example():
    assert sort_numbers("three one five") == "one three five"


def test_empty_string():
    assert sort_numbers("") == ""


def test_single_number():
    assert sort_numbers("five") == "five"


def test_numbers_already_sorted():
    assert sort_numbers("zero one two three four") == "zero one two three four"


def test_numbers_in_reverse_order():
    assert sort_numbers("nine eight seven six five four three two one zero") == (
        "zero one two three four five six seven eight nine"
    )


def test_numbers_in_random_order():
    assert sort_numbers("seven two nine one five") == "one two five seven nine"


def test_all_numbers_are_identical():
    assert sort_numbers("three three three") == "three three three"


def test_duplicate_numbers():
    assert sort_numbers("five one five two one") == "one one two five five"


def test_zero_and_nine_boundaries():
    assert sort_numbers("nine zero nine zero") == "zero zero nine nine"


def test_all_valid_number_words():
    assert sort_numbers(
        "five two eight zero three nine one seven four six"
    ) == "zero one two three four five six seven eight nine"


def test_leading_spaces():
    assert sort_numbers("  three one") == "one three"


def test_trailing_spaces():
    assert sort_numbers("three one  ") == "one three"


def test_multiple_consecutive_spaces():
    assert sort_numbers("three  one   two") == "one two three"


def test_only_spaces():
    assert sort_numbers("   ") == ""


def test_two_numbers_in_reverse_order():
    assert sort_numbers("two one") == "one two"


def test_numbers_with_repeated_zero():
    assert sort_numbers("zero nine zero one") == "zero zero one nine"


def test_invalid_number_word_raises_key_error():
    with pytest.raises(KeyError):
        sort_numbers("one ten two")


def test_mixed_valid_and_invalid_words_raise_key_error():
    with pytest.raises(KeyError):
        sort_numbers("three invalid one")


def test_numeric_digits_raise_key_error():
    with pytest.raises(KeyError):
        sort_numbers("1 2 3")


def test_sorting_preserves_duplicate_counts():
    result = sort_numbers("four two four one two")
    assert result.split() == ["one", "two", "two", "four", "four"]