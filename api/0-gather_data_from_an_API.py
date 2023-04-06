#!/usr/bin/python3 
""" Request a Rest API"""


import json
import requests
from sys import argv


if __name__ == '__main__':
    '''code'''
    emp_id = int(argv[1])
    emp_name = ''
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    users = requests.get(users_url)
    tasks = requests.get(todo_url)

    for user in users.json():
        if user['id'] == emp_id:
            emp_name = user['name']
            break

    task_ok = 0
    total_task = 0
    task_title =[]

    for tsk in tasks.json():
        if tsk['userId'] == emp_id:
            total_task += 1
            if tsk['completed']:
                task_ok += 1
                task_title.append(tsk['title'])

    print('Employee {} is done with tasks({}/{}):'.format(emp_name, task_ok, total_task))

    for title in task_title:
        print('\t {}'.format(title))
