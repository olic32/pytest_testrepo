from lib.class_diary import *
import pytest

def test_class_diary_format_storage():

#When a new entry is created, it is stored correctly as local variables

    entry = DiaryEntry("01/01/2000", "Happy new year to me!")
    assert entry.title == "01/01/2000"
    assert entry.contents == "Happy new year to me!"

#When format is called, returns a string with title and contens nicely laid out:

    assert entry.format() == "01/01/2000 : Happy new year to me!"

def test_count_words():

#when called, returns the number of whole words in the entry
#would assume this is just the contents, not the title
#This should include single letter words, and double spaces/misttypes



    entry = DiaryEntry("25/12/2000", "Happy Christmas to me!")

    assert entry.count_words() == 4

    entry_2 = DiaryEntry("25/12/2000", "  Happy Christmas to me! l l")

    assert entry_2.count_words() == 6

#CHeck the edge case of no words in contents or title

    entry_3 = DiaryEntry("","")
    
    assert entry_3.count_words() == 0


def test_reading_time():

    #when called, uses the wpm given as arg and calculates wpm for content stored locally

    entry = DiaryEntry("13/13/2030", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of  (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, , comes from a line in section 1.10.32.")

    assert entry.count_words() == 120

    assert entry.reading_time(60) == 2

    assert entry.reading_time(60.0) == 2

    #no need to worry about floats or decimals - it uses count words which always returns int
    # 


def test_reading_chunk():

    entry = DiaryEntry("13/13/2040", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of  (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, , comes from a line in section 1.10.32.")

    #when called, returns the two arguments times together # of words

    assert entry.reading_chunk(5,2) == "Contrary to popular belief, Lorem Ipsum is not simply random"

    # when called again on the same instance, returns the same but starting
    # from where the previous return left off

    assert entry.reading_chunk(5,2) == "text. It has roots in a piece of classical Latin"

    # when called multiple times, loops back round to the start of the stext

    entry_2 = DiaryEntry("10/10/1349", "Caught the plague. Again. Why do I keep catching plague.")

    assert entry_2.reading_chunk(4,2) == "Caught the plague. Again. Why do I keep"

    assert entry_2.reading_chunk(4,2) == "catching plague. Caught the plague. Again. Why do"

    entry_3 = DiaryEntry("Hello", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur,")


    assert entry_3.reading_chunk(4,10) == "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia,"

    assert entry_3.reading_chunk(4,10) == "looked up one of the more obscure Latin words, consectetur, Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
