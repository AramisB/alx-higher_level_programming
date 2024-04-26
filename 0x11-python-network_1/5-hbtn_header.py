#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])

    try:
        req_hId = r.headers['X-Request-Id']
        print(req_hId)
    except URLError as e:
        pass
