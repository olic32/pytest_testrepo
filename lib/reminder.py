class Reminder():
    def __init__(self, name):
        self.name = name
        self.task = None
    def remind_me(self,task):
        self.task = task
    def remind(self):
        if self.task is None:
            raise Exception("No task has been set!")
        return f"{self.name}, {self.task}"
    
