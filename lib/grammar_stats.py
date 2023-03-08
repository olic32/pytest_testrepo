class GrammarStats:
    def __init__(self):
        self.checks_passed = 0
        self.checks_attempted = 0

    def check(self, text):

        self.checks_attempted += 1

        has_caps = False
        has_punc = False



        correct_punctuation = "!?."

        if text[:1] == text[:1].upper():
            has_caps = True

        if text[-1] in correct_punctuation:
            has_punc = True


        if has_caps and has_punc:
            self.checks_passed += 1 
            return True
        else:
            return False
        
        
        


    def percentage_good(self):
        if self.checks_attempted > 0:
            percent_passed =  str(int(100 / (self.checks_attempted / self.checks_passed)))
            return f"{percent_passed}%"
        else:
            raise Exception("No checks made!")
