#!/usr/bin/python3
"""
 a Python script that takes in a URL,
 sends a request to the URL
 and displays the body of the response (decoded in utf-8)
 Manage urllib.error.HTTPError exceptions
 and print: Error code: followed by the HTTP status code
"""
import urllib.request


if __name__ == "__main__":
    import urllib
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            html_str = html.decode('utf-8')
            print(html_str)
    except urllib.error.HTTPError as e:
        print('Error Code: ', e.code)
