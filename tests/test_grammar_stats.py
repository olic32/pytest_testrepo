from lib.grammar_stats import *

import pytest

# {{PROBLEM}} Function Design Recipe

# a class with 2 funtions, one checks for grammar
# the other checks what percentage of previous checks have passed

## 1. Describe the Problem

#as above

## 2. Design the Function Signature

# def __init__:
    #self.pass_count - to keep track of how mnay have passed



#def check(self,text)

# Parameters: just text, which is to be checked

# Returns: boolean

# Side Effects: none



#def percentage_good(self)

# Parameters: none

# Returns: percentage as float

# Side Effects: none



def test_grammer_stats():

    #checks if a correct sentence returns as True

    test_text = GrammarStats()

    assert test_text.check("Hello, me name is Oliver.") == True

    #checks if an incorrect sentence is False

    assert test_text.check("hello my name is oliver") == False

    #Checks if just one of either fails the test

    assert test_text.check("hello my name is oliver.") == False
    assert test_text.check("Hello my name is oliver") == False

    #Checks if a percentage 100% is returned if one check passed

    test_text_2 = GrammarStats()

    assert test_text_2.check("Hello, me name is Oliver.") == True

    assert test_text_2.percentage_good() == "100%"

    #Check if when a false check is made, the percetage changes to 50

    assert test_text_2.check("hello, me name is Oliver") == False

    assert test_text_2.percentage_good() == "50%"

    #Check if a percent check made but no checks, recieve errpr

    test_text_3 = GrammarStats()

    with pytest.raises(Exception) as e:
        test_text_3.percentage_good()
    error_message = str(e.value)
    assert error_message == "No checks made!"

