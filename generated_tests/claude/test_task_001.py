import pytest
from solutions.task_001 import separate_paren_groups


def test_docstring_example():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']


def test_empty_string():
    assert separate_paren_groups('') == []


def test_only_spaces():
    assert separate_paren_groups('     ') == []


def test_single_simple_group():
    assert separate_paren_groups('()') == ['()']


def test_single_simple_group_with_spaces():
    assert separate_paren_groups('( )') == ['()']


def test_single_nested_group():
    assert separate_paren_groups('(())') == ['(())']


def test_deeply_nested_group():
    assert separate_paren_groups('((((()))))') == ['((((()))))']


def test_two_simple_groups_no_spaces():
    assert separate_paren_groups('()()') == ['()', '()']


def test_two_simple_groups_with_space():
    assert separate_paren_groups('() ()') == ['()', '()']


def test_many_simple_groups():
    assert separate_paren_groups('()()()()()') == ['()'] * 5


def test_mixed_nested_and_simple_groups():
    assert separate_paren_groups('() (()) ((())) (()())') == [
        '()', '(())', '((()))', '(()())'
    ]


def test_group_with_sibling_children():
    assert separate_paren_groups('(()())') == ['(()())']


def test_group_with_multiple_levels_and_siblings():
    assert separate_paren_groups('((())(()))') == ['((())(()))']


def test_spaces_inside_group_are_removed():
    assert separate_paren_groups('( ( ) ( ) )') == ['(()())']


def test_leading_and_trailing_spaces():
    assert separate_paren_groups('   ()   (())   ') == ['()', '(())']


def test_many_spaces_between_groups():
    assert separate_paren_groups('()          (())') == ['()', '(())']


def test_spaces_between_every_character():
    assert separate_paren_groups(' ( ( ) ) ( ) ') == ['(())', '()']


def test_tabs_and_newlines_ignored():
    assert separate_paren_groups('(\t)\n(\n(\t))') == ['()', '(())']


def test_result_is_list_of_strings():
    result = separate_paren_groups('() (())')
    assert isinstance(result, list)
    assert all(isinstance(group, str) for group in result)


def test_order_of_groups_preserved():
    assert separate_paren_groups('((())) () (())') == ['((()))', '()', '(())']


def test_each_returned_group_is_balanced():
    result = separate_paren_groups('(()) () ((())()) (()())')
    for group in result:
        depth = 0
        for c in group:
            depth += 1 if c == '(' else -1
            assert depth >= 0
        assert depth == 0


def test_concatenated_groups_equal_input_without_spaces():
    s = '(()) () ((())()) (()())'
    result = separate_paren_groups(s)
    assert ''.join(result) == s.replace(' ', '')


def test_unclosed_trailing_group_is_dropped():
    # Unbalanced input: incomplete group is never appended
    assert separate_paren_groups('()(') == ['()']


def test_only_open_parens_returns_empty():
    assert separate_paren_groups('(((') == []


def test_only_close_paren_creates_unexpected_group():
    # depth becomes -1, never returns to 0 -> nothing appended
    assert separate_paren_groups(')') == []


def test_close_then_open_unbalanced():
    # ')' -> depth -1, '(' -> depth 0 -> appends ')('
    assert separate_paren_groups(')(') == [')(']


def test_large_input_many_groups():
    s = '(())' * 500
    assert separate_paren_groups(s) == ['(())'] * 500


def test_large_deep_nesting():
    s = '(' * 500 + ')' * 500
    assert separate_paren_groups(s) == [s]


def test_input_with_non_paren_characters_ignored():
    assert separate_paren_groups('(a) (b(c))') == ['()', '(())']


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ('', []),
        ('()', ['()']),
        ('(())', ['(())']),
        ('() ()', ['()', '()']),
        ('(()) ()', ['(())', '()']),
        ('(()()) ()', ['(()())', '()']),
        ('( ) ( ( ) )', ['()', '(())']),
        ('((()()))(())', ['((()()))', '(())']),
    ],
)
def test_parametrized_cases(input_string, expected):
    assert separate_paren_groups(input_string) == expected