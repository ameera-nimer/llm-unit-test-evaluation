import pytest
from solutions.task_023 import strlen


def test_docstring_example_empty():
    assert strlen('') == 0


def test_docstring_example_abc():
    assert strlen('abc') == 3


def test_single_character():
    assert strlen('a') == 1


def test_two_characters():
    assert strlen('ab') == 2


def test_word():
    assert strlen('hello') == 5


def test_sentence_with_spaces():
    assert strlen('hello world') == 11


def test_single_space():
    assert strlen(' ') == 1


def test_only_spaces():
    assert strlen('     ') == 5


def test_leading_and_trailing_spaces_counted():
    assert strlen('  a  ') == 5


def test_digits():
    assert strlen('12345') == 5


def test_punctuation():
    assert strlen('!@#$%') == 5


def test_newline_counts_as_one_character():
    assert strlen('\n') == 1


def test_tab_counts_as_one_character():
    assert strlen('\t') == 1


def test_mixed_whitespace_characters():
    assert strlen('a\nb\tc ') == 6


def test_carriage_return_newline_counts_two():
    assert strlen('\r\n') == 2


def test_null_character_counts():
    assert strlen('\x00') == 1


def test_escaped_backslash_is_single_character():
    assert strlen('\\') == 1


def test_raw_string_backslash_n_is_two_characters():
    assert strlen(r'\n') == 2


def test_uppercase_and_lowercase():
    assert strlen('AbCdE') == 5


def test_unicode_accented_characters():
    assert strlen('éàü') == 3


def test_unicode_non_latin_characters():
    assert strlen('你好世界') == 4


def test_unicode_cyrillic():
    assert strlen('привет') == 6


def test_unicode_emoji_single_code_point():
    assert strlen('😀') == 1


def test_unicode_multiple_emoji():
    assert strlen('😀😃😄') == 3


def test_length_counts_code_points_not_bytes():
    s = 'é'
    assert strlen(s) == 1
    assert len(s.encode('utf-8')) == 2


def test_combining_character_counts_separately():
    # 'e' followed by combining acute accent is two code points
    assert strlen('e\u0301') == 2


def test_precomposed_vs_decomposed_differ():
    assert strlen('\u00e9') == 1
    assert strlen('e\u0301') == 2


def test_long_string():
    assert strlen('a' * 10000) == 10000


def test_very_long_string():
    assert strlen('ab' * 100000) == 200000


def test_length_of_concatenation_is_sum():
    a, b = 'hello', 'world!!'
    assert strlen(a + b) == strlen(a) + strlen(b)


def test_length_of_repetition():
    assert strlen('abc' * 7) == 21


def test_length_of_slice():
    s = 'abcdefgh'
    assert strlen(s[2:5]) == 3


def test_matches_builtin_len():
    for s in ['', 'a', 'abc', 'hello world', '😀😃', '\n\t', 'x' * 123]:
        assert strlen(s) == len(s)


def test_result_is_non_negative():
    for s in ['', 'a', 'abc', ' ', '\n']:
        assert strlen(s) >= 0


def test_empty_string_is_only_zero_length_for_nonempty_check():
    assert strlen('') == 0
    assert strlen(' ') != 0


def test_returns_int_type():
    assert isinstance(strlen('abc'), int)
    assert isinstance(strlen(''), int)


def test_input_not_modified():
    s = 'abc'
    strlen(s)
    assert s == 'abc'


def test_deterministic_repeated_calls():
    assert strlen('hello') == strlen('hello')


def test_list_input_returns_length():
    assert strlen([1, 2, 3]) == 3


def test_tuple_input_returns_length():
    assert strlen((1, 2)) == 2


def test_bytes_input_returns_byte_length():
    assert strlen(b'abc') == 3


def test_integer_input_raises_type_error():
    with pytest.raises(TypeError):
        strlen(123)


def test_float_input_raises_type_error():
    with pytest.raises(TypeError):
        strlen(3.14)


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        strlen(None)


@pytest.mark.parametrize(
    "string, expected",
    [
        ('', 0),
        ('a', 1),
        ('ab', 2),
        ('abc', 3),
        (' ', 1),
        ('  ', 2),
        ('a b', 3),
        ('\n', 1),
        ('\t\t', 2),
        ('12345', 5),
        ('hello world', 11),
        ('éé', 2),
        ('😀', 1),
        ('你好', 2),
        ('x' * 100, 100),
    ],
)
def test_parametrized_cases(string, expected):
    assert strlen(string) == expected