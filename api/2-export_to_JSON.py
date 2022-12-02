#!/usr/bin/python3
"""Python script to export data in the JSON format"""

from requests import get
from sys import argv
import json

if __name__ == '__main__':
    res = get('https://jsonplaceholder.typicode.com/todos/')
    details = res.json()

    row = []
    res2 = get('https://jsonplaceholder.typicode.com/users/')
    details1 = res2.json()

    for count in details1:
        if count['id'] == int(argv[1]):
            employee = count['username']
            id_no = count['id']

    row = []

    for count in details:
        new_dict = {}
        if count['userId'] == int(argv[1]):
            new_dict['username'] = employee
            new_dict['task'] = count['title']
            new_dict['completed'] = count['completed']
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + '.json', 'w') as file:
        file.write(json_obj)
