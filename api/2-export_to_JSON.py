#!/usr/bin/python3
"""
script to export data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    '''code'''
    emp_id = int(argv[1])
    f_name = "{}.json".format(emp_id)
    eN = ''
    us_name = ''
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    users = requests.get(users_url)
    tasks = requests.get(todo_url)

    for user in users.json():
        if user['id'] == emp_id:
            eN = user['name']
            us_name = user['username']
            break

    # Format must be:
    # { "USER_ID": [{"task": "TASK_TITLE",
    #               "completed": TASK_COMPLETED_STATUS,
    #               "username": "USERNAME"},
    #               {"task": "TASK_TITLE",
    #               "completed": TASK_COMPLETED_STATUS,
    #               "username": "USERNAME"},
    #                   ... ]}

    data = {}
    datos = []
    line = {}
    for tsk in tasks.json():
        line["task"] = tsk["title"]
        line["completed"] = tsk["completed"]
        line["username"] = us_name
        datos.append(line)
    data[emp_id] = datos

    with open(f_name, 'w') as file:
        json.dump(data, file)
