#!/usr/bin/python3
''' Script that returns information about a given employee ID
and his/her TODO list
'''

from requests import get
from sys import argv


if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos/')
    details = res.json()
    completed = 0
    total = 0
    tasks = []
    res1 = get('https://jsonplaceholder.typicode.com/users/')
    details1 = res1.json()

    for count in details1:
        if count.get('id') == int(argv[1]):
            employee = count.get('name')

    for count in details:
        if count.get('userId') == int(argv[1]):
            total += 1

            if count.get('completed') is True:
                completed += 1
                tasks.append(count.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee,
                                                          completed, total))

    for count in tasks:
        print("\t {}".format(count))
