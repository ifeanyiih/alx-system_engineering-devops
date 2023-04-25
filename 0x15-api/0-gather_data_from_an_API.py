#!/usr/bin/python3
""" a Python script that, using a REST API,
for a given employee ID, returns information about his/her
TODO list progress.
"""

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
            userTodo.append(todo.copy())

    completed = 0
    for todo in userTodo:
        if todo['completed']:
            completed = completed + 1

    print('Employee {} is done with tasks({}/{}):'
          .format(user['name'], completed, len(userTodo)))
    for todo in userTodo:
        if todo['completed']:
            print('\t {}'.format(todo['title']))
