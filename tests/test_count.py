from lib.counter import *

def test_counter():
    my_counter = Counter()
    my_counter.add(10)
    my_counter_2 = Counter()
    my_counter_2.add(1)
    my_counter_2.add(3)

    assert my_counter.report() == "Counted to 10 so far."
    assert my_counter_2.report() == "Counted to 4 so far."
