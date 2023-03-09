class TaskManager():
    def __init__(self):
        self.task_list = []

    def add_a_task(self,task):

        if type(task) != str:
            raise Exception("Wrong data type!")
        else:
            self.task_list.append(task)
        
    def show_tasklist(self):
        return self.task_list
    
    def remove_a_task(self,task):
        if task in self.task_list:
            self.task_list.remove(task)


