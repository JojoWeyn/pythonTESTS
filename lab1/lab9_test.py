#Сайланкин Дамир 107b

import pytest
from lab9 import multiply, divide, distance, quadratic, geometric_sum

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(7, -3) == -21
    assert multiply(-4, -5) == 20

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(0, 5) == 0
    assert divide(7, -7) == -1
    with pytest.raises(ValueError):
        divide(1, 0)

def test_distance():
    assert distance(0, 0, 3, 4) == 5
    assert distance(1, 1, 1, 1) == 0
    assert distance(-1, -1, 2, 2) == 4.242640687119285
    assert distance(1, 2, 4, 6) == 5
    assert distance(0, 0, 0, 0) == 0

def test_quadratic():
    assert quadratic(1, -3, 2) == (2, 1)
    assert quadratic(1, 2, 1) == (-1, -1)
    assert quadratic(1, 0, -4) == (2, -2)
    assert quadratic(1, -2, 5) == None
    assert quadratic(1, 4, 4) == (-2, -2)

def test_geometric_sum():
    assert geometric_sum(2, 3, 3) == 26
    assert geometric_sum(1, 2, 5) == 31
    assert geometric_sum(1, 1, 5) == 5
    assert geometric_sum(5, 0.5, 4) == 9.375
    assert geometric_sum(1, 0, 10) == 1
