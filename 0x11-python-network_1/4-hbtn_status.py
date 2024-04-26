#!/usr/bin/python3
"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
 using the requests package
"""


if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t - type: {}'.format(type(r.content)))
    print('\t - content: {}'.format(r.content))
