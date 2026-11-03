from solutions.task_019 import sort_numbers


def test_sort_numbers_empty():
    assert sort_numbers("") == ""


def test_sort_numbers_single():
    assert sort_numbers("five") == "five"


def test_sort_numbers_docstring_example():
    assert sort_numbers("three one five") == "one three five"


def test_sort_numbers_already_sorted():
    assert sort_numbers("zero one two three four") == "zero one two three four"


def test_sort_numbers_reverse_sorted():
    assert sort_numbers("nine eight seven six") == "six seven eight nine"


def test_sort_numbers_duplicates():
    assert sort_numbers("two zero two one zero") == "zero zero one two two"


def test_sort_numbers_extra_spaces():
    assert sort_numbers("  three   one   five  ") == "one three five"