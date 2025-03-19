import os
import sys
from script import addition


sys.path.insert(0, os.getcwd())


def test_addition_instance():
    assert isinstance(addition(1, 2), int)

