#!/usr/bin/python3
""" a Python script that, using a REST API,
for a given employee ID, returns information about his/her
TODO list progress.
"""

import json
import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    user = user.json()
    r = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = r.json()
    userTodo = []
    for todo in todos:
        if todo['userId'] == user['id']:
           task = {}
           task['task'] = todo['title']
           task['completed'] = todo['completed']
           task['username'] = user['username']
           userTodo.append(task)
    taskObj = {"{}".format(userId): userTodo}

    with open('{}.json'.format(userId), 'w') as file:
        json.dump(taskObj, file)

        with open('{}.json'.format(userId), 'w') as file:
            json.dump(taskObj, file)

            with open('{}.json'.format(userId), 'w') as file:
                json.dump(taskObj, file)
