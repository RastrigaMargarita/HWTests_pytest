import pytest

from utils import arrs

test_data_get = [[[1, 2, 3], 1, "test", 2],
                 [[1, 2, 3], -1, None, None],
                 [[1, 2, 3], -153, "test", "test"],
                 [[1, 2, 3], 1, "test", 2]]

test_data_slice = [[[1, 2, 3, 4], 1, 3, [2, 3]],
                   [[1, 2, 3], 1, None, [2, 3]],
                   [[1, 2, 3], -1, None, [3]],
                   [[1, 2, 3], -115, 2, [1, 2]],
                   [[], 0, 2, []]]


@pytest.mark.parametrize("arr, one, two, expected", test_data_get)
def test_get(arr, one, two, expected):
    assert arrs.get(arr, one, two) == expected


def test_get_er():
    with pytest.raises(IndexError):
        assert arrs.get([], 0)


@pytest.mark.parametrize("arr, one, two, expected", test_data_slice)
def test_slice(arr, one, two, expected):
    assert arrs.my_slice(arr, one, two) == expected
