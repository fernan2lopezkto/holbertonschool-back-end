#!/usr/bin/python3
"""script"""


import json
import sys
from urllib import request

if __name__ == "__main__":
    # var
    total_task = 0
    task_ok = 0
    employee_ID = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users"

    resp = requests.get(url_user).json()

    '''
    # recuest for users
    response = request.urlopen(url_user)
    users = response.read().decode("utf-8")
    list = json.loads(users)

    # recuest for task
    response_task = request.urlopen(url)
    tasks = response_task.read().decode("utf-8")
    list_task = json.loads(tasks)


    # found name of user by id
    for i in list:
        if i["id"] == employee_ID:
            emp_name = i["name"]

    # work with task
    for task in list_task:
        if task['userId'] == employee_ID:
            total_task = total_task + 1
            if task["completed"] == True:
                task_ok = task_ok + 1

    '''            
    # EMPLOYEE_NAME: name of the employee

    # output first line
    l1output = "Employee {} is done with tasks({}/{}):".format()

    print(l1output)
