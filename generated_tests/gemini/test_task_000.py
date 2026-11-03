from solutions.task_000 import has_close_elements


def test_has_close_elements_empty_list():
    assert has_close_elements([], 0.5) is False


def test_has_close_elements_single_element():
    assert has_close_elements([1.0], 0.5) is False


def test_has_close_elements_no_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False


def test_has_close_elements_with_close_elements():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) is True


def test_has_close_elements_duplicates():
    assert has_close_elements([1.0, 1.0], 0.5) is True


def test_has_close_elements_boundary_equal_threshold():
    # Distance is exactly 0.5. Since the condition is strict (< threshold), it should return False.
    assert has_close_elements([1.0, 1.5], 0.5) is False


def test_has_close_elements_boundary_just_below_threshold():
    # Distance is 0.499, which is less than 0.5, so it should return True.
    assert has_close_elements([1.0, 1.499], 0.5) is True


def test_has_close_elements_negative_numbers():
    assert has_close_elements([-1.0, -1.2, -3.0], 0.3) is True
    assert has_close_elements([-1.0, -2.0, -3.0], 0.5) is False
