#!/usr/bin/python3
"""A script that uses the urllib module to fetch a url"""

if __name__ == "__main__":
    import urllib.request

    req = urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
    with req as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))
