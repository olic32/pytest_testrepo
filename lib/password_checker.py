class PasswordChecker():
    def __init__(self):
        pass
    def check(self,password):
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid Pass")
        
