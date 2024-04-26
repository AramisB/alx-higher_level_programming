#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the body of the response
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    if __name__ == '__main__':
        r = requests.get(argv[1])
        status = r.status_code
        print(r.text) if status < 400 else print(
            "Error code: {}".format(r.status_code))
