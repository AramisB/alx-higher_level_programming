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
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
