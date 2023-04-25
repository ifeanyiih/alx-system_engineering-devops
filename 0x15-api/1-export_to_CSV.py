#!/usr/bin/python3
""" a Python script that, using a REST API,
for a given employee ID, returns information about his/her
TODO list progress.
"""

import csv
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

    with open('{}.csv'.format(userId), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for todo in userTodo:
            writer.writerow([userId, user['username'], todo['completed'], todo['title']])
