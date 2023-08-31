from utils.dicts import get_val


def test_get():
    assert get_val([1, 2, 3], 1, "test") == 2
    assert get_val([], 0, "test") == "test"
    assert get_val([1, 2, 3], 4) == "git"
