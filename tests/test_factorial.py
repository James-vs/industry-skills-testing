import pytest
from mymath.factorial import factorial


def test_1():
    assert factorial(3) == 6


def test_2():
    assert factorial(5) == 120


def test_3():
    assert factorial(0) == 1


def test_4_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_5_string():
    with pytest.raises(TypeError):
        factorial("wobble")
