import json

from project import *
from utilities import *
from user import *
from user_manager import *

class ProjectCreator:
    def __init__(self):
        pass


    def create_empty(self, user_id):
        with open(str(user_id) +"_projects.json", "w") as f:
            f.writelines("[]")


class ProjectManager:
    def __init__(self, user_id):
        user_id_str = str(user_id)
        print("Project manager initialized with user_id: ".format(user_id_str))
        self.projects = []
        with open(user_id_str +"_projects.json", "r") as f:
            file_content = f.read()
            self.projects = json.loads(file_content, object_hook=projects_json_decoder)


    def add_project(self, name, description, priority, progress, start_date, end_date, status, tasks):
        '''
        Adding new project
        '''
        self.projects.append(Project(name, description, priority, progress, start_date, end_date, status, tasks))

    
    def delete_projects(self, name):
        '''
        Deleting project
        '''
        i = 0
        for project in self.projects:
            if project.name == name:
                del self.projects[i]
                return
            i += 1
         

    def write_json(self, user_id):
        user_id_str = str(user_id)
        print("write_json called with user_id: ".format(user_id_str))
        with open(user_id_str +"_projects.json", "w") as f:
            f.writelines(json.dumps(self.projects, cls = ProjectEncoder, indent=4, ensure_ascii=False))


    def get_project_count(self):
        return len(self.projects)


    def get_projects(self):
        return self.projects

    
    def get_project_by_name(self, name) -> Project:
        for project in self.projects:
            if project.name == name:
                return project

    def get_project_names(self) -> list:
        ret = []
        for project in self.projects:
            ret.append(project.name)
        return ret
