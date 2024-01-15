import pytest
import source.functions as functions
import time


def test_add():
    result = functions.add(1, 4)
    assert result == 5


def test_add_strings():
    result = functions.add("i like", " burgers")
    assert result == "i like burgers"


def test_divide():
    result = functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        functions.divide(10, 0)


# slow is user-defined and not part of pytest.mark
@pytest.mark.slow
def test_slow():
    time.sleep(3)


@pytest.mark.skip(reason="This feature is currently unavailable")
def test_skip():
    pass


@pytest.mark.xfail(reason="We cannot divide by zero")
def test_xfail():
    test_divide_by_zero()
