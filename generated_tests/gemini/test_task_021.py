from solutions.task_021 import rescale_to_unit


def test_rescale_to_unit_docstring_example():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]


def test_rescale_to_unit_two_elements():
    assert rescale_to_unit([10.0, 20.0]) == [0.0, 1.0]


def test_rescale_to_unit_negative_numbers():
    assert rescale_to_unit([-10.0, 0.0, 10.0]) == [0.0, 0.5, 1.0]


def test_rescale_to_unit_unordered_list():
    assert rescale_to_unit([3.0, 1.0, 5.0]) == [0.5, 0.0, 1.0]


def test_rescale_to_unit_floats_precision():
    result = rescale_to_unit([1.5, 2.5, 3.5])
    expected = [0.0, 0.5, 1.0]
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-7