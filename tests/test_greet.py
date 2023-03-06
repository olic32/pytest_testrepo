from lib.greet import *

def test_greet():
    result = greet("James")
    assert result == "Hello, James!"

