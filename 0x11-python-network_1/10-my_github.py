#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    access_token = sys.argv[2]
    url = 'https://api.github.com/user'
    headers = {'Authorization': 'token {}'.format(access_token)}

    r = requests.get(url, headers=headers).json()
    if 'id' in r:
        print(r['id'])
    else:
        print(None)
