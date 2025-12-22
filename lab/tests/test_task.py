import pytest
from lab.task import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        divide(10, 0)