#!/usr/bin/python3
""" Request a Rest API"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    '''code'''
    emp_id = int(argv[1])
    f_name = "{}.csv".format(emp_id)
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

    #Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    #File name must be: USER_ID.csv

    with open(f_name, 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for tsk in tasks.json():
            if tsk["userId"] == emp_id:
                t_Ok = tsk["completed"]
                t_Ttle = tsk["title"]
                writer.writerow([emp_id, us_name, t_Ok, t_Ttle])
