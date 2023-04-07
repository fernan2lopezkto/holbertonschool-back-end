#!/usr/bin/python3
""" Request a Rest API"""


import requests
from sys import argv


if __name__ == '__main__':
    '''code'''
    emp_id = int(argv[1])
    eN = ''
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    users = requests.get(users_url)
    tasks = requests.get(todo_url)
    for user in users.json():
        if user['id'] == emp_id:
            eN = user['name']
            break

    tOK = 0
    tTL = 0
    task_title = []

    for tsk in tasks.json():
        if tsk['userId'] == emp_id:
            tTL += 1
            if tsk['completed']:
                tOK += 1
                task_title.append(tsk['title'])

    print('Employee {} is done with tasks({}/{}):'.format(eN, tOK, tTL))

    for title in task_title:
        print('\t {}'.format(title))
