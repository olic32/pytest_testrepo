
from lib.challenge import *
import pytest


#Check the class exists, and check that a list is returned when the method is called
#when called returns empty list

def test_show_list():
    test_musictracker = MusicTracker()

    assert test_musictracker.show_list() == "No tracks in library"

#check when add_list called, then show list, returns list with the additiona

def test_add_and_show():
    test_musictracker = MusicTracker()

    test_musictracker.add_a_track("Song")

    assert test_musictracker.show_list() == "In your library, you have Song"


#check that the track added is a string
def test_add_wrong_data_type():
    test_musictracker = MusicTracker()

    with pytest.raises(Exception) as e_info:
        test_musictracker.add_a_track(12)
    error_message = str(e_info.value)

    assert error_message == "Wrong data type!"

    

#check if returns correct with mulitple tracks

def test_add_multiple_tracks():
    test_musictracker = MusicTracker()

    test_musictracker.add_a_track("Song")
    test_musictracker.add_a_track("Song2")
    test_musictracker.add_a_track("Song3")


    assert test_musictracker.show_list() == "In your library, you have Song, Song2, Song3"

#check if allows adding two tracks with same name

def test_add_duplicates():
    test_musictracker = MusicTracker()

    test_musictracker.add_a_track("Song")
    test_musictracker.add_a_track("Song")

    assert test_musictracker.show_list() == "In your library, you have Song"

    


