#!/usr/bin/python3 
""" Request a Rest API""" 
import json 
import requests 
from sys import argv

if __name__ == '__main__':
    '''code'''
    emp_id = int(argv[1])
    todo_url = ''
    users_url = ''
    
    users = requests.get(users_url)
    tasks = requests.get(todo_url)
  