from lib.gratitudes import *

def test_gratitudes_functions():
    tester = Gratitudes()
    tester.add("Tea")
    tester.add("Biscuits")
    assert tester.format() == "Be grateful for: Tea, Biscuits"