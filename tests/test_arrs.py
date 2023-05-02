import pytest

from utils import arrs

@pytest.fixture
def test_data_get():
    return [[[1, 2, 3], 1, "test", 2],
           [[1, 2, 3], -1, "test", "test"],
           [[1, 2, 3], 1, "test", 2]]

@pytest.fixture
def test_data_slice():
    return [[[1, 2, 3, 4], 1, 3, [2, 3]],
            [[1, 2, 3], 1, None, [2, 3]],
            [[1, 2, 3], -115, None, [1, 2, 3]]]

def test_get(test_data_get):
    for data_item in test_data_get:
        assert arrs.get(data_item[0], data_item[1], data_item[2]) == data_item[3]
    with pytest.raises(IndexError):
        assert arrs.get([], 0)


def test_slice(test_data_slice):
    for data_item in test_data_slice:
        assert arrs.my_slice(data_item[0], data_item[1], data_item[2]) == data_item[3]
    with pytest.raises(AssertionError):
        assert arrs.my_slice([], 8)
