
import pytest

from solutions.task_006 import parse_nested_parens


def test_docstring_example():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]


def test_empty_string():
    assert parse_nested_parens("") == []


def test_single_empty_parenthesis_group():
    assert parse_nested_parens("()") == [1]


def test_single_level_nesting():
    assert parse_nested_parens("(())") == [2]


def test_two_levels_of_nesting():
    assert parse_nested_parens("(()())") == [2]


def test_three_levels_of_nesting():
    assert parse_nested_parens("((()))") == [3]


def test_deeply_nested_parentheses():
    assert parse_nested_parens("((((()))))") == [5]


def test_multiple_simple_groups():
    assert parse_nested_parens("() () ()") == [1, 1, 1]


def test_multiple_groups_with_different_depths():
    assert parse_nested_parens("() (()) ((())) (((())))") == [1, 2, 3, 4]


def test_groups_without_spaces_between_characters():
    assert parse_nested_parens("()()") == [1, 1]


def test_groups_with_multiple_spaces_between_them():
    assert parse_nested_parens("()   (())    ((()))") == [1, 2, 3]


def test_leading_and_trailing_spaces():
    assert parse_nested_parens("  () (()) ((()))  ") == [1, 2, 3]


def test_only_spaces():
    assert parse_nested_parens("     ") == []


def test_group_with_sibling_nested_groups():
    assert parse_nested_parens("(()())") == [2]


def test_multiple_sibling_nested_groups():
    assert parse_nested_parens("(()()) ((())(()))") == [2, 3]


def test_nested_and_non_nested_groups():
    assert parse_nested_parens("() (()()) ((()))") == [1, 2, 3]


def test_maximum_depth_at_the_beginning():
    assert parse_nested_parens("((())())") == [3]


def test_maximum_depth_at_the_end():
    assert parse_nested_parens("(()(()))") == [3]


def test_maximum_depth_in_the_middle():
    assert parse_nested_parens("(()())") == [2]


def test_many_sibling_groups_inside_outer_parentheses():
    assert parse_nested_parens("(()()()())") == [2]


def test_long_sequence_of_simple_groups():
    assert parse_nested_parens(" ".join(["()"] * 100)) == [1] * 100


def test_long_deeply_nested_group():
    depth = 50
    group = "(" * depth + ")" * depth
    assert parse_nested_parens(group) == [depth]


def test_result_is_a_list():
    result = parse_nested_parens("() (())")
    assert isinstance(result, list)


def test_result_contains_integers():
    result = parse_nested_parens("() (()) ((()))")
    assert all(isinstance(depth, int) for depth in result)


def test_group_with_unequal_sibling_depths():
    assert parse_nested_parens("((())(()))") == [3]


def test_deep_group_followed_by_shallow_group():
    assert parse_nested_parens("((((())))) ()") == [5, 1]


def test_shallow_group_followed_by_deep_group():
    assert parse_nested_parens("() (((())))") == [1, 4]


def test_multiple_groups_with_repeated_depths():
    assert parse_nested_parens("(()) (()) ((())) ((()))") == [2, 2, 3, 3]


def test_deepest_nesting_is_not_total_parenthesis_count():
    assert parse_nested_parens("(()()())") == [2]


def test_nested_groups_with_varied_structure():
    assert parse_nested_parens("((())()(()))") == [3]


@pytest.mark.parametrize(
    "paren_string, expected",
    [
        ("", []),
        ("()", [1]),
        ("(())", [2]),
        ("((()))", [3]),
        ("(()())", [2]),
        ("(()(()))", [3]),
        ("() ()", [1, 1]),
        ("(()) ((()))", [2, 3]),
        ("(((()))) () (())", [4, 1, 2]),
        ("(()()) ((())) () ((())()())", [2, 3, 1, 3]),
    ],
)
def test_various_parenthesis_groups(paren_string, expected):
    assert parse_nested_parens(paren_string) == expected


def test_result_length_matches_number_of_groups():
    assert len(parse_nested_parens("() (()) ((()))")) == 3


def test_group_order_is_preserved():
    assert parse_nested_parens("((())) () (())") == [3, 1, 2]


def test_each_group_has_at_least_one_level():
    result = parse_nested_parens("() (()) ((()))")
    assert all(depth >= 1 for depth in result)
