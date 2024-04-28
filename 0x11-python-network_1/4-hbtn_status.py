#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t - type: {}".format(type(r.content)))
    print("\t - content: {}".format(r.content))
