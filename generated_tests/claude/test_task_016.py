import pytest
from solutions.task_016 import count_distinct_characters


def test_docstring_example_case_insensitive():
    assert count_distinct_characters('xyzXYZ') == 3


def test_docstring_example_jerry():
    assert count_distinct_characters('Jerry') == 4


def test_empty_string():
    assert count_distinct_characters('') == 0


def test_single_character():
    assert count_distinct_characters('a') == 1


def test_single_uppercase_character():
    assert count_distinct_characters('A') == 1


def test_same_letter_different_case():
    assert count_distinct_characters('aA') == 1


def test_all_identical_characters():
    assert count_distinct_characters('aaaaaa') == 1


def test_all_identical_mixed_case():
    assert count_distinct_characters('aAaAaA') == 1


def test_all_distinct_lowercase():
    assert count_distinct_characters('abcdef') == 6


def test_all_distinct_uppercase():
    assert count_distinct_characters('ABCDEF') == 6


def test_all_distinct_mixed_case():
    assert count_distinct_characters('aBcDeF') == 6


def test_repeated_characters_counted_once():
    assert count_distinct_characters('hello') == 4


def test_word_with_mixed_case_repeats():
    assert count_distinct_characters('Mississippi') == 4


def test_full_lowercase_alphabet():
    assert count_distinct_characters('abcdefghijklmnopqrstuvwxyz') == 26


def test_full_alphabet_both_cases():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    assert count_distinct_characters(alphabet + alphabet.upper()) == 26


def test_digits():
    assert count_distinct_characters('1234567890') == 10


def test_repeated_digits():
    assert count_distinct_characters('112233') == 3


def test_letters_and_digits():
    assert count_distinct_characters('a1b2c3') == 6


def test_space_counts_as_character():
    assert count_distinct_characters('a b') == 3


def test_only_spaces():
    assert count_distinct_characters('     ') == 1


def test_leading_and_trailing_spaces_counted():
    assert count_distinct_characters(' a ') == 2


def test_punctuation():
    assert count_distinct_characters('!@#$%') == 5


def test_repeated_punctuation():
    assert count_distinct_characters('!!!???') == 2


def test_newline_and_tab_are_distinct_characters():
    assert count_distinct_characters('a\n\t') == 3


def test_newline_repeated():
    assert count_distinct_characters('\n\n\n') == 1


def test_unicode_characters():
    assert count_distinct_characters('éèê') == 3


def test_unicode_case_insensitive():
    assert count_distinct_characters('éÉ') == 1


def test_non_latin_case_insensitive():
    assert count_distinct_characters('ДД дд') == 2


def test_greek_letters_case_folding():
    assert count_distinct_characters('αΑβΒ') == 2


def test_emoji():
    assert count_distinct_characters('😀😀😃') == 2


def test_digits_unaffected_by_lowercasing():
    assert count_distinct_characters('1a1A') == 2


def test_result_never_exceeds_string_length():
    for s in ['', 'a', 'abc', 'aaa', 'AaBb', 'hello world']:
        assert count_distinct_characters(s) <= len(s)


def test_result_equals_length_when_all_distinct():
    s = 'abcdefg'
    assert count_distinct_characters(s) == len(s)


def test_order_independence():
    assert count_distinct_characters('abcABC123') == count_distinct_characters('3c2b1aCBA')


def test_concatenation_with_itself_unchanged():
    s = 'Hello World'
    assert count_distinct_characters(s + s) == count_distinct_characters(s)


def test_upper_and_lower_variants_equal():
    s = 'Hello World'
    assert count_distinct_characters(s.upper()) == count_distinct_characters(s.lower())
    assert count_distinct_characters(s.upper()) == count_distinct_characters(s)


def test_matches_reference_implementation():
    for s in ['Python', 'Programming', 'AbCdEfG', 'The quick brown fox', 'a1!A1!']:
        assert count_distinct_characters(s) == len(set(s.lower()))


def test_long_string_single_character():
    assert count_distinct_characters('a' * 10000) == 1


def test_long_string_cycling_alphabet():
    s = ''.join(chr(ord('a') + i % 26) for i in range(5000))
    assert count_distinct_characters(s) == 26


def test_long_string_many_distinct_code_points():
    s = ''.join(chr(0x4E00 + i) for i in range(1000))
    assert count_distinct_characters(s) == 1000


def test_returns_int_type():
    assert isinstance(count_distinct_characters('abc'), int)
    assert isinstance(count_distinct_characters(''), int)


def test_input_not_modified():
    s = 'AbC'
    count_distinct_characters(s)
    assert s == 'AbC'


def test_non_string_input_raises_attribute_error():
    with pytest.raises(AttributeError):
        count_distinct_characters(123)


def test_none_input_raises_attribute_error():
    with pytest.raises(AttributeError):
        count_distinct_characters(None)


@pytest.mark.parametrize(
    "string, expected",
    [
        ('', 0),
        ('a', 1),
        ('A', 1),
        ('aA', 1),
        ('ab', 2),
        ('aB', 2),
        ('xyzXYZ', 3),
        ('Jerry', 4),
        ('hello', 4),
        ('HELLO', 4),
        ('abc123', 6),
        ('  ', 1),
        ('a a', 2),
        ('Aa Bb', 3),
        ('!!!', 1),
    ],
)
def test_parametrized_cases(string, expected):
    assert count_distinct_characters(string) == expected