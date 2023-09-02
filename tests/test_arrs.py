import pytest

from utils.arrs import get, my_slice

@pytest.fixture()
def coll():
    return [1, 2, 3]

def test_get(coll):
    a = coll
    assert get(a, 1) == 2
    assert get([], 0) == None


def test_slice(coll):
    a = coll
    assert my_slice(a) == [1, 2, 3]
    assert my_slice(a, 1, 3) == [2, 3]
    assert my_slice([], 10, 20) == []
    assert my_slice([1, 2], 1, 20) == [2]
