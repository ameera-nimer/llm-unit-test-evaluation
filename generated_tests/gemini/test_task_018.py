from solutions.task_018 import how_many_times


def test_how_many_times_empty_string():
    assert how_many_times("", "a") == 0


def test_how_many_times_empty_substring():
    # Depending on how the function handles an empty substring:
    # range(len(string) - len('') + 1) -> range(len(string) + 1)
    # string[i:i] == '' is True for all i, so it counts len(string) + 1 times.
    assert how_many_times("abc", "") == 4


def test_how_many_times_docstring_examples():
    assert how_many_times("", "a") == 0
    assert how_many_times("aaa", "a") == 3
    assert how_many_times("aaaa", "aa") == 3


def test_how_many_times_no_match():
    assert how_many_times("hello", "xyz") == 0


def test_how_many_times_overlapping():
    assert how_many_times("banana", "ana") == 2


def test_how_many_times_substring_longer_than_string():
    assert how_many_times("abc", "abcd") == 0


def test_how_many_times_exact_match():
    assert how_many_times("test", "test") == 1