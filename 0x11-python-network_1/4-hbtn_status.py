#!/usr/bin/python3
"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
 using the requests package
"""


if __name__ == "__main__":
    import requests

    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
