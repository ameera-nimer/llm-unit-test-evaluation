from solutions.task_017 import parse_music


def test_parse_music_empty_string():
    assert parse_music("") == []


def test_parse_music_docstring_example():
    assert parse_music("o o| .| o| o| .| .| .| .| o o") == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]


def test_parse_music_single_notes():
    assert parse_music("o") == [4]
    assert parse_music("o|") == [2]
    assert parse_music(".|") == [1]


def test_parse_music_multiple_spaces():
    assert parse_music("o   o|    .|") == [4, 2, 1]


def test_parse_music_mixed_sequence():
    assert parse_music(".| o .| o|") == [1, 4, 1, 2]