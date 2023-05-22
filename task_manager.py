from task import *

class TaskManager():
    def __init__(self):
        self.tasks = []


    def add_task(self, project, name, description, priority, start_date, end_date, status):
        '''
        Adding new task
        '''
        task = Task(name, project.name, description, priority, start_date, end_date, status)
        self.tasks.append(task)
        project.tasks.append(task)

    def delete_tasks(self, name):
        '''
        Deleting tasks
        '''
        # self.tasks = [task for task in self.tasks if task.project_name != project_name]

        i = 0
        for task in self.tasks:
            if task.name == name:
                del self.tasks[i]
                return
            i += 1

    def get_all_tasks(self):
        return self.tasks

    def get_tasks(self, project_name):
        tasks = [task for task in self.tasks if task.project_name == project_name]
        return tasks


    def sync_tasks(self, project_manager):
        self.tasks = []
        for project in project_manager.get_projects():
            self.tasks += project.tasks
            
    def count_tasks(self) -> int:
        return len(self.tasks)
    
    def get_task_by_name(self, name) -> Task:
        for task in self.tasks:
            if task.name == name:
                return task