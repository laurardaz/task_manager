import sys

from task import *
from project import *
from user import *

def projects_json_decoder(d):
    if "project_name" in d:
        return Task(d["name"], d["project_name"], d["description"], d["priority"], d["start_date"], d["end_date"], d["status"])
    elif "tasks" in d:
        return Project(d["name"], d["description"], d["priority"], d["progress"], d["start_date"], d["end_date"], d["status"], d["tasks"])
    elif "users" in d:
        return User(d["id"], d["user_name"], d["password"], d["email"])
    else:
        sys.exit("Couldn't parse JSON")

def user_json_decoder(d):
    if "user_name" in d:
        return User(d["id"], d["user_name"], d["password"], d["email"])
    else:
        sys.exit("Couldn't parse JSON")
