from utils.dicts import get_val
import pytest

@pytest.mark.parametrize('coll, index, defo, result', [
    ([1, 2, 3], 1, 'test', 2),
    ([1, 2, 3], 10, 'test', 'test'),
    ([], 1, 'git', 'git'),
    ([1, 2, 3], -2, None, None),
])


def test_get(coll, index, defo, result ):
    assert get_val(coll, index, defo) == result
