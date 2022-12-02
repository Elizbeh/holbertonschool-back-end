#!/usr/bin/python3
"""Python script to export data in the JSON format"""

from requests import get
import json

if __name__ == '__main__':
    res = get('https://jsonplaceholder.typicode.com/todos/')
    details = res.json()

    row = []
    res1 = get('https://jsonplaceholder.typicode.com/users/')
    details1 = res1.json()

    new_dict1 = {}

    for j in details1:
        row = []
        for i in details:
            new_dict2 = {}
            if j['id'] == i['userId']:
                new_dict2['username'] = j['username']
                new_dict2['task'] = i['title']
                new_dict2['completed'] = i['completed']
                row.append(new_dict2)
        new_dict1[j['id']] = row

    with open("todo_all_employees.json", 'w') as file:
        json_obj = json.dumps(new_dict1)
        file.write(json_obj)
