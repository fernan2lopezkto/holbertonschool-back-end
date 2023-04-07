#!/usr/bin/python3
""" Request a Rest API"""

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

    """
    for tsk in tasks.json():
        if tsk['userId'] == emp_id:
            tTL += 1
            if tsk['completed']:
                tOK += 1
                task_title.append(tsk['title'])
    """
                
    # Format must be: 
    # { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
    #               {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
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

'''
    with open(f_name, 'w') as f:
        writer = csv.writer(f, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for tsk in tasks.json():
            if tsk["userId"] == emp_id:
                t_Ok = tsk["completed"]
                t_Ttle = tsk["title"]
                writer.writerow([emp_id, us_name, t_Ok, t_Ttle])

'''
