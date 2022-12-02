#!/usr/bin/python3
"""Python script to export data in the CSV format"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    res = get('https://jsonplaceholder.typicode.com/todos/')
    details = res.json()

    row = []
    res2 = get('https://jsonplaceholder.typicode.com/users/')
    details2 = res2.json()

    for i in details2:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in details:
            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                writ.writerow(row)
