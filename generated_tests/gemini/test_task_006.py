from solutions.task_006 import parse_nested_parens


def test_parse_nested_parens_docstring_example():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]


def test_parse_nested_parens_empty_string():
    assert parse_nested_parens('') == []


def test_parse_nested_parens_single_group():
    assert parse_nested_parens('((()))') == [3]


def test_parse_nested_parens_multiple_spaces():
    assert parse_nested_parens('   (()())   ((()))   ') == [2, 3]


def test_parse_nested_parens_simple_parentheses():
    assert parse_nested_parens('() (()) ((()))') == [1, 2, 3]


def test_parse_nested_parens_complex_group():
    assert parse_nested_parens('((((()))))') == [5]