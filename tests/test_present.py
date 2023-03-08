import pytest

from lib.present import *

def test_present_class():
    tester = Present()

    with pytest.raises(Exception) as e_info:
        tester.unwrap()
    error_message = str(e_info.value)

    assert error_message == "Nothing in this present!"



def test_present_other():
    tester_2 = Present()
    tester_2.wrap("Gift")

    with pytest.raises(Exception) as e_info:
        tester_2.wrap("AnotherGift")
    error_message = str(e_info.value)

    assert error_message == "A contents has already been wrapped"