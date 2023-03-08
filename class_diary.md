# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

Create a basic diary entry management software



## 2. Design the Function Signature


class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        pass

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        pass

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass

## 3. Create Examples as Tests

#When a new entry is created, it is stored correctly as local variables

entry = DiaryEntry("01/01/2000", "Happy new year to me!")
entry.title -> "01/01/2000"
entry.contents -> "Happy new year to me!"

#When format is called, returns a string with title and contens nicely laid out:

entry = DiaryEntry("01/01/2000", "Happy new year to me!")
entry.format() -> "01/01/2000 : Happy new year to me!"





## 4. Implement the Behaviour

1st test failure - diary entry not defined
    Code diary entry __init__ function / passes
2nd failure - no format defined
    code format function / passes
