#!/usr/bin/python3
"""
a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        r = requests.post(url, data={'q': sys.argv[1]})
    else:
        r = requests.post(url, data={'q': ""})

    try:
        if r.json() == {}:
            print('No result')
        else:
            print('{[]} {}'.format(r.json().get('id')), r.json().get('name'))
    except ValueError:
        print('Not a valid JSON')
