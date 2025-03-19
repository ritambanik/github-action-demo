import os
import sys
from script import addition


sys.path.insert(0, os.getcwd())


def test_addition():
    assert addition(1, 2) == 3
    assert addition(5, 5) == 10
    assert addition(10, 10) == 20
