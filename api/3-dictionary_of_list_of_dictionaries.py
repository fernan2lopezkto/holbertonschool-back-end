#!/usr/bin/python3
""" 
script to export data in the JSON format
"""

import json
import requests

if __name__ == '__main__':
    '''code'''
    data = {}
    datos = []
    f_name = "todo_all_employees.json"
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    users = requests.get(users_url)
    tasks = requests.get(todo_url)

    for user in users.json():
        emp_id = user['id']
        us_name = user['username']
        for tsk in tasks.json():
            if tsk["userId"] == emp_id:
                line = {}
                line["username"] = us_name
                line["task"] = tsk["title"]
                line["completed"] = tsk["completed"]
                datos.append(line)
        data[emp_id] = datos

    # Format must be:
    # { "USER_ID": [
    #       {"username": "USERNAME",
    #        "task": "TASK_TITLE",
    #        "completed": TASK_COMPLETED_STATUS},
    #       {"username": "USERNAME",
    #        "task": "TASK_TITLE",
    #        "completed": TASK_COMPLETED_STATUS},
    #           ... ],
    #   "USER_ID": [
    #       {"username": "USERNAME",
    #        "task": "TASK_TITLE",
    #        "completed": TASK_COMPLETED_STATUS},
    #       {"username": "USERNAME", ...}, ... ]}

    with open(f_name, 'w') as file:
        json.dump(data, file)
