#!/usr/bin/python3
"""script"""

import sys
from urllib import request

if __name__ == "__main__":
    employee_ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users"

    reaponse = request.urlopen(url_user)
        for i in request:
            if i[id] = employee_ID:
                print(i[name])