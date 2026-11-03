from solutions.task_016 import count_distinct_characters


def test_count_distinct_characters_empty():
    assert count_distinct_characters("") == 0


def test_count_distinct_characters_single():
    assert count_distinct_characters("a") == 1


def test_count_distinct_characters_docstring_examples():
    assert count_distinct_characters("xyzXYZ") == 3
    assert count_distinct_characters("Jerry") == 4


def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters("aA") == 1


def test_count_distinct_characters_duplicates():
    assert count_distinct_characters("hello world") == 8


def test_count_distinct_characters_special_chars_and_numbers():
    assert count_distinct_characters("a1!A") == 3