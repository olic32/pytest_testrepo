from lib.exercise_1 import *
import pytest

#First, check we can access the tasklist

def test_check_list():
    test_manager = TaskManager()
    assert test_manager.show_tasklist() == []


#Check if we can add an item to the list, and then show it

def test_add_item_show():
    test_manager = TaskManager()
    test_manager.add_a_task("Walk the dog")

    assert test_manager.show_tasklist() == ["Walk the dog"]

#See if when another task is added, you see both tasks
    test_manager.add_a_task("Put the washing out")

    assert test_manager.show_tasklist() == ["Walk the dog", "Put the washing out"]



#check if an error message is received when a non str is input

def test_add_improper_item():
    test_manager = TaskManager()
    
    with pytest.raises(Exception) as e:
        test_manager.add_a_task({12:9})
    error_message = str(e.value)

    assert error_message == "Wrong data type!"

#check list empty after adding and removing 1 task

def test_remove_from_list():
    test_manager = TaskManager()

    test_manager.add_a_task("Walk the dog")

    test_manager.remove_a_task("Walk the dog")

    assert test_manager.show_tasklist() == []

#check list changed after adding two tasks andf removing only one

def test_remove_from_list_2():
    test_manager = TaskManager()

    test_manager.add_a_task("Walk the dog")

    test_manager.add_a_task("Wash clothes")

    test_manager.remove_a_task("Walk the dog")

    assert test_manager.show_tasklist() == ["Wash clothes"]

#check to see if no error if trying to remove task from list that isnt in list

def test_remove_from_list_3():
    test_manager = TaskManager()

    test_manager.add_a_task("Walk the dog")

    test_manager.remove_a_task("Wash clothes")

    assert test_manager.show_tasklist() == ["Walk the dog"]