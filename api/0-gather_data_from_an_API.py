#!/usr/bin/python3
"""script"""


import json
import sys
from urllib import request

if __name__ == "__main__":
    employee_ID = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users"

    response = request.urlopen(url_user)
    
    users = response.read().decode("utf-8")

    list = json.loads(users)

    for i in list:
        if i["id"] == employee_ID:
            emp_name = i["name"]

    l1output = "Employee {} is done with tasks(8/20):".format(emp_name)

    print(l1output)
