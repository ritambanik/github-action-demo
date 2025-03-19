import os, sys

sys.path.insert(0, os.getcwd())

from script import addition

def test_addition_instance():
    assert isinstance(addition(1, 2), int)
