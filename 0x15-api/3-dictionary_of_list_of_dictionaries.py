#!/usr/bin/python3
""" a Python script that, using a REST API,
for a given employee ID, returns information about his/her
TODO list progress.
"""

import json
import requests
import sys

if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    users = users.json()
    r = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = r.json()
    taskObj = {}
    for user in users:
        userTodo = []
        for todo in todos:
            if todo['userId'] == user['id']:
                task = {}
                task['username'] = user['username']
                task['task'] = todo['title']
                task['completed'] = todo['completed']
                userTodo.append(task)
        taskObj["{}".format(user['id'])] = userTodo

    with open('todo_all_employees.json', 'w') as file:
        json.dump(taskObj, file)
