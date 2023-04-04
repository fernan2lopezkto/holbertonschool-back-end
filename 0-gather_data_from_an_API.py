#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress. """


from urllib import request
import sys

# take employee ID
employee_ID = sys.argv[1]

# formated the url with the employee ID
url = "https://jsonplaceholder.typicode.com/todos/{}".format(employee_ID)

# make request and save in 'html' var
with request.urlopen(url) as response:
   html = response.read()

# format output to example:
# Employee Ervin Howell is done with tasks(8/20):

#EMPLOYEE_NAME = url[name] # name of the employee
#NUMBER_OF_DONE_TASKS = # number of completed tasks
#TOTAL_NUMBER_OF_TASKS = # total number of tasks

print(html)
