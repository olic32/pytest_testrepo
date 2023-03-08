from lib.reminder import *
import pytest



def test_remind_user_task():
    reminder = Reminder("Oliver")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No task has been set!"


