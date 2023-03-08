from lib.string_builder import *

def test_string_builder_functions():
    tester = StringBuilder()
    tester.add("Hello ")
    tester.add("World")
    assert tester.size() == 11
    assert tester.output() == "Hello World"