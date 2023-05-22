import json

from user import *
from utilities import *

class UserManager:
    def __init__(self):
        self.users = []
        with open("users.json", "r") as f:
            file_content = f.read()
            self.users = json.loads(file_content, object_hook=user_json_decoder)

    def max_id(self):
        m = 0
        for user in self.users:
            m = max(int(user.id), m)
        return m

    
    def add_new_user(self, user_name, password, email):
        self.users.append(User(self.max_id() + 1, user_name, password, email))


    def write_user_json(self):
        with open("users.json", "w") as f:
            f.writelines(json.dumps(self.users, cls = ProjectEncoder, indent=4, ensure_ascii=False))

    
    def check_user(self, user_name, password):
        for user in self.users:
            if user.user_name == user_name and user.password == password:
                return True
        return False


    def get_user_id(self, name):
        for user in self.users:
            if user.user_name == name:
                print("found user with id: {}".format(user.id))
                return user.id
        sys.exit("Couldn't find user", name)


    def set_current_user(self, user_name: str):
        self.current_user = user_name
