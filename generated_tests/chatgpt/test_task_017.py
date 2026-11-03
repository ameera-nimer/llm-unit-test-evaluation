import pytest
from solutions.task_017 import parse_music


def test_docstring_example():
    assert parse_music("o o| .| o| o| .| .| .| .| o o") == [
        4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4
    ]


def test_empty_string():
    assert parse_music("") == []


def test_single_whole_note():
    assert parse_music("o") == [4]


def test_single_half_note():
    assert parse_music("o|") == [2]


def test_single_quarter_note():
    assert parse_music(".|") == [1]


def test_all_whole_notes():
    assert parse_music("o o o") == [4, 4, 4]


def test_all_half_notes():
    assert parse_music("o| o| o|") == [2, 2, 2]


def test_all_quarter_notes():
    assert parse_music(".| .| .|") == [1, 1, 1]


def test_mixed_notes():
    assert parse_music("o .| o|") == [4, 1, 2]


def test_leading_space():
    assert parse_music(" o o|") == [4, 2]


def test_trailing_space():
    assert parse_music("o o| ") == [4, 2]


def test_multiple_consecutive_spaces():
    assert parse_music("o  o|   .|") == [4, 2, 1]


def test_only_spaces():
    assert parse_music("   ") == []


def test_note_order_is_preserved():
    assert parse_music(".| o o| .|") == [1, 4, 2, 1]


def test_repeated_notes():
    assert parse_music("o| o| o| o|") == [2, 2, 2, 2]


def test_many_notes():
    music = "o o| .| " * 100
    assert parse_music(music) == [4, 2, 1] * 100


def test_invalid_note_raises_key_error():
    with pytest.raises(KeyError):
        parse_music("x")


def test_mixed_valid_and_invalid_notes_raise_key_error():
    with pytest.raises(KeyError):
        parse_music("o o| x .|")