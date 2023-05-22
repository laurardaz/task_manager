import json

class User:
    def __init__(self, id, user_name, password, email):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.email = email
    
   
class ProjectEncoder(json.JSONEncoder):
        def default(self, obj):
            return obj.__dict__

class UserEncoder(json.JSONEncoder):
        def default(self, obj):
            return obj.__dict__