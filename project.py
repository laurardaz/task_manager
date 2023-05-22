import json

class Project:
    def __init__(self, name, description, priority, progress, start_date, end_date, status, tasks):
        self.name = name
        self.description = description
        self.priority = priority
        self.progress = progress
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.tasks = tasks


    def tasks_count(self):
        return len(self.tasks)


    def remove_task(self, name):
        i = 0
        for task in self.tasks:
            if task.name == name:
                del self.tasks[i]
                return
            i += 1
   

class ProjectEncoder(json.JSONEncoder):
        def default(self, obj):
            return obj.__dict__


