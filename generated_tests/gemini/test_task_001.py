from solutions.task_001 import separate_paren_groups


def test_separate_paren_groups_empty():
    assert separate_paren_groups("") == []


def test_separate_paren_groups_docstring_example():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']


def test_separate_paren_groups_single_group():
    assert separate_paren_groups('((()))') == ['((()))']


def test_separate_paren_groups_multiple_simple_groups():
    assert separate_paren_groups('()()()') == ['()', '()', '()']


def test_separate_paren_groups_with_spaces():
    assert separate_paren_groups(' ( )   ( ( ) ) ') == ['()', '(())']


def test_separate_paren_groups_complex_nested():
    assert separate_paren_groups('(())(())') == ['(())', '(())']