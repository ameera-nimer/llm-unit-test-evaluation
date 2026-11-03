import pytest
from solutions.task_006 import parse_nested_parens


def test_docstring_example():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]


def test_empty_string():
    assert parse_nested_parens('') == []


def test_only_spaces():
    assert parse_nested_parens('     ') == []


def test_single_simple_group():
    assert parse_nested_parens('()') == [1]


def test_single_nested_group_depth_two():
    assert parse_nested_parens('(())') == [2]


def test_single_nested_group_depth_three():
    assert parse_nested_parens('((()))') == [3]


def test_deep_nesting():
    assert parse_nested_parens('(((((())))))') == [6]


def test_group_with_siblings_depth_two():
    assert parse_nested_parens('(()())') == [2]


def test_group_with_siblings_depth_one():
    assert parse_nested_parens('()()()') == [1]


def test_group_with_uneven_branches():
    assert parse_nested_parens('(()(()))') == [3]


def test_deepest_nesting_at_start():
    assert parse_nested_parens('((()))()') == [3]


def test_deepest_nesting_at_end():
    assert parse_nested_parens('()((()))') == [3]


def test_deepest_nesting_in_middle():
    assert parse_nested_parens('()((()))()') == [3]


def test_two_groups():
    assert parse_nested_parens('() (())') == [1, 2]


def test_multiple_groups_increasing_depth():
    assert parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]


def test_multiple_groups_decreasing_depth():
    assert parse_nested_parens('(((()))) ((())) (()) ()') == [4, 3, 2, 1]


def test_multiple_identical_groups():
    assert parse_nested_parens('(()) (()) (())') == [2, 2, 2]


def test_many_simple_groups():
    assert parse_nested_parens(' '.join(['()'] * 10)) == [1] * 10


def test_leading_space_ignored():
    assert parse_nested_parens(' () (())') == [1, 2]


def test_trailing_space_ignored():
    assert parse_nested_parens('() (()) ') == [1, 2]


def test_leading_and_trailing_spaces_ignored():
    assert parse_nested_parens('   ()   (())   ') == [1, 2]


def test_multiple_spaces_between_groups():
    assert parse_nested_parens('()      ((()))') == [1, 3]


def test_output_length_matches_group_count():
    result = parse_nested_parens('() (()) ((())) (()())')
    assert len(result) == 4


def test_order_of_groups_preserved():
    assert parse_nested_parens('((())) () (())') == [3, 1, 2]


def test_result_is_list_of_ints():
    result = parse_nested_parens('() (())')
    assert isinstance(result, list)
    assert all(isinstance(depth, int) for depth in result)


def test_all_depths_positive_for_balanced_groups():
    result = parse_nested_parens('() (()) ((())) (()())')
    assert all(depth >= 1 for depth in result)


def test_large_depth():
    s = '(' * 500 + ')' * 500
    assert parse_nested_parens(s) == [500]


def test_many_large_groups():
    groups = ['(' * n + ')' * n for n in range(1, 51)]
    assert parse_nested_parens(' '.join(groups)) == list(range(1, 51))


def test_wide_group_does_not_increase_depth():
    s = '(' + '()' * 100 + ')'
    assert parse_nested_parens(s) == [2]


def test_only_closing_parens_gives_zero_depth():
    # depth never rises above zero -> max_depth stays 0
    assert parse_nested_parens(')))') == [0]


def test_only_opening_parens_counts_depth():
    # no validation of balance: max depth reached is 3
    assert parse_nested_parens('(((') == [3]


def test_unbalanced_group_reports_max_reached():
    assert parse_nested_parens('(()') == [2]


def test_close_before_open_group():
    # depth: -1, 0 -> max_depth stays 0 after first '(' reaches 0 (not > 0)
    assert parse_nested_parens(')(') == [0]


def test_close_then_open_then_deeper():
    # depth: -1, 0, 1 -> max_depth 1
    assert parse_nested_parens(')((') == [1]


def test_tabs_not_treated_as_separators():
    # only ' ' splits; a tab is treated as a non-'(' char (decrements depth)
    assert parse_nested_parens('()\t()') == [1]


@pytest.mark.parametrize(
    "paren_string, expected",
    [
        ('', []),
        (' ', []),
        ('()', [1]),
        ('(())', [2]),
        ('() ()', [1, 1]),
        ('(()) ()', [2, 1]),
        ('(()()) ((())) () ((())()())', [2, 3, 1, 3]),
        ('((()()))', [3]),
        ('(()(())) ()', [3, 1]),
        ('   (())   ((()))   ', [2, 3]),
    ],
)
def test_parametrized_cases(paren_string, expected):
    assert parse_nested_parens(paren_string) == expected