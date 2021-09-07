import pytest

def inx(x):
    return x+1

def test_answer():
    assert inx(4)==5
