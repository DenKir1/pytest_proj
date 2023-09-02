from utils.dicts import get_val
import pytest

@pytest.mark.parametrize('coll, key, defo, result', [
    ({'a': 1, 'b': 2, 'c': 3}, 'b', 'test', 2),
    ({'a': 1, 'b': 2, 'c': 3}, 10, 'test', 'test'),
    ({}, 1, 'git', 'git'),
    ({'a': 1, 'b': 2, 'c': 3}, -2, None, None),
])


def test_get(coll, key, defo, result ):
    assert get_val(coll, key, defo) == result
