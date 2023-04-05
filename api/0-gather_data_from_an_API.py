#!/usr/bin/python3
"""script"""

import sys
from urllib import request

if __namr__ == "__main__":
  employee_ID = sys.argv[1]
  url = "https://jsonplaceholder.typicode.com/todos"
  url_user = "https://jsonplaceholder.typicode.com/users"

"""
  # make request and save in 'html' var
  with request.urlopen(url) as response:
   html = response.read()

# format output to example:
# Employee Ervin Howell is done with tasks(8/20):

#EMPLOYEE_NAME = url[name] # name of the employee
#NUMBER_OF_DONE_TASKS = # number of completed tasks
#TOTAL_NUMBER_OF_TASKS = # total number of tasks

print(html)
"""
