
import pytest

from solutions.task_001 import separate_paren_groups


def test_empty_string():
    assert separate_paren_groups("") == []


def test_single_empty_parenthesis_group():
    assert separate_paren_groups("()") == ["()"]


def test_single_nested_group():
    assert separate_paren_groups("(())") == ["(())"]


def test_deeply_nested_group():
    assert separate_paren_groups("(((())))") == ["(((())))"]


def test_multiple_separate_groups():
    assert separate_paren_groups("()()()") == ["()", "()", "()"]


def test_multiple_groups_with_different_depths():
    assert separate_paren_groups("()(())((()))") == ["()", "(())", "((()))"]


def test_example_from_docstring():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]


def test_spaces_between_groups():
    assert separate_paren_groups("() () (())") == ["()", "()", "(())"]


def test_spaces_inside_parentheses():
    assert separate_paren_groups("( ( ) )") == ["(())"]


def test_only_spaces():
    assert separate_paren_groups("     ") == []


def test_leading_and_trailing_spaces():
    assert separate_paren_groups("  () (())  ") == ["()", "(())"]


def test_many_nested_groups():
    assert separate_paren_groups("((((()))))") == ["((((()))))"]


def test_nested_groups_followed_by_simple_group():
    assert separate_paren_groups("((()))()") == ["((()))", "()"]


def test_simple_group_followed_by_nested_groups():
    assert separate_paren_groups("()((()))") == ["()", "((()))"]


def test_groups_with_varying_nesting_depths():
    assert separate_paren_groups("()(())((()))(((())))") == [
        "()",
        "(())",
        "((()))",
        "(((())))",
    ]


def test_adjacent_groups_without_spaces():
    assert separate_paren_groups("(())()((()))") == ["(())", "()", "((()))"]


def test_groups_separated_by_multiple_spaces():
    assert separate_paren_groups("()     (())       ((()))") == [
        "()",
        "(())",
        "((()))",
    ]


def test_spaces_between_nested_parentheses():
    assert separate_paren_groups("( ( ( ) ) )") == ["((()))"]


def test_group_with_many_sibling_subgroups():
    assert separate_paren_groups("(()()())") == ["(()()())"]


def test_multiple_groups_with_sibling_subgroups():
    assert separate_paren_groups("(()())((()()))") == ["(()())", "((()()))"]


def test_group_with_alternating_nesting():
    assert separate_paren_groups("((())(()))") == ["((())(()))"]


def test_long_sequence_of_simple_groups():
    input_string = "()" * 100
    assert separate_paren_groups(input_string) == ["()"] * 100


def test_long_sequence_of_nested_groups():
    input_string = "(" * 50 + ")" * 50
    assert separate_paren_groups(input_string) == [input_string]


def test_input_with_newline_and_tab_whitespace():
    assert separate_paren_groups("()\n\t(())") == ["()", "(())"]


def test_group_containing_only_open_and_close_parentheses():
    assert separate_paren_groups("((()))") == ["((()))"]


def test_multiple_groups_with_whitespace_inside_and_between():
    assert separate_paren_groups(" ( ( ) )   ( ( ( ) ) ) ") == [
        "(())",
        "((()))",
    ]


def test_return_type_is_list():
    result = separate_paren_groups("()")
    assert isinstance(result, list)


def test_each_result_is_a_string():
    result = separate_paren_groups("()(())")
    assert all(isinstance(group, str) for group in result)


def test_output_groups_are_balanced():
    groups = separate_paren_groups("()(())((()))")

    for group in groups:
        depth = 0
        for char in group:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            assert depth >= 0
        assert depth == 0


def test_output_contains_no_whitespace():
    result = separate_paren_groups(" ( ( ) )  ( ) ")
    assert result == ["(())", "()"]
    assert all(not any(char.isspace() for char in group) for group in result)


def test_concatenating_output_preserves_parenthesis_order():
    input_string = "(()())((()))()"
    result = separate_paren_groups(input_string)
    assert "".join(result) == input_string


def test_whitespace_only_between_parentheses_is_ignored():
    assert separate_paren_groups("( \t ( \n ) \t )") == ["(())"]
