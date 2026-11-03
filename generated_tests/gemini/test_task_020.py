from solutions.task_020 import find_closest_elements


def test_find_closest_elements_docstring_examples():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)


def test_find_closest_elements_two_elements():
    assert find_closest_elements([5.5, 1.2]) == (1.2, 5.5)


def test_find_closest_elements_negative_numbers():
    assert find_closest_elements([-1.5, -1.0, 0.0, 3.0]) == (-1.5, -1.0)


def test_find_closest_elements_identical_elements():
    assert find_closest_elements([4.5, 4.5, 10.0]) == (4.5, 4.5)


def test_find_closest_elements_mixed_order():
    assert find_closest_elements([10.0, 1.1, 1.2, 20.0]) == (1.1, 1.2)