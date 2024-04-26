#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(sys.argv[1], sys.argv[2])).json()
    if 'id' in req:
        print(req['id'])
    else:
        print('None')
