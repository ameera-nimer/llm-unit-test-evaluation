from solutions.task_007 import filter_by_substring


def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'a') == []


def test_filter_by_substring_docstring_example():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']


def test_filter_by_substring_no_matches():
    assert filter_by_substring(['dog', 'cat', 'bird'], 'fish') == []


def test_filter_by_substring_all_matches():
    assert filter_by_substring(['apple', 'appetizer', 'apply'], 'app') == ['apple', 'appetizer', 'apply']


def test_filter_by_substring_empty_substring():
    assert filter_by_substring(['hello', 'world'], '') == ['hello', 'world']


def test_filter_by_substring_case_sensitivity():
    assert filter_by_substring(['Apple', 'banana', 'APRICOT'], 'a') == ['Apple', 'banana']