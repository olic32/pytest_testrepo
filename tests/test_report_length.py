from lib.report_length import *

def test_report_length():
    assert report_length("123 123 123") == "This string was 11 characters long."
    assert report_length("1") == "This string was 1 characters long."
