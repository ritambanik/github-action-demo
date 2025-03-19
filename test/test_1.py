import os
import sys

sys.path.insert(0, os.getcwd())

from script import addition


def test_addition():
    assert addition(1, 2) == 3
    assert addition(5, 5) == 10
    assert addition(10, 10) == 20
