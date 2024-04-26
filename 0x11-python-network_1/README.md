Fetching Internet Resources with Python
This guide explores various methods for fetching internet resources and manipulating data from external services using Python. It combines the strengths of urllib.request (for basic scenarios) and requests (the recommended library for most cases).

Fetching Resources:

1. Using urllib.request (Basic):

Import:
import urllib.request

Open URL:
with urllib.request.urlopen('https://www.example.com/') as response:
    data = response.read()  # Raw bytes
Decode Response (if applicable):

Python
if response.headers.get_content_charset() is not None:
    data = data.decode(response.headers.get_content_charset())
else:
    # Handle cases where charset is unknown (fallback encoding)

2. Using requests (Recommended):

Install: pip install requests (if not already installed)

Import:
import requests

Make Request:
response = requests.get('https://www.example.com/')

Check Response Status:
if response.status_code == 200:
    data = response.text  # Decoded text (assumes UTF-8)
    # Or: data = response.content  # Raw bytes
else:
    print(f"Error: {response.status_code}")

Decoding urllib Response:
Determine Encoding: Use response.headers.get_content_charset() to get the character encoding from server headers.
Decode Based on Encoding: If known, use .decode(encoding).
Fallback Encoding: Use a fallback encoding (like latin-1 or utf-8) with caution, as it can lead to errors. Consider libraries like chardet for automatic detection.

Using requests:
requests automatically handles decoding for most common encodings (usually UTF-8).
For custom encodings, specify as an option:
response = requests.get('https://example.com/', encoding='your_encoding')

Making HTTP Requests:
GET: requests.get(url)
POST: requests.post(url, data=your_data). You can also send JSON data with json=your_json_data.
PUT/etc.: Use requests.put(url, data=your_data) or the appropriate method for the specific HTTP verb.

Fetching JSON Resources:
Use requests.get(url):
response = requests.get('https://api.example.com/data.json')
if response.status_code == 200:
    data = response.json()  # Parses JSON response into a Python object

Manipulating External Service Data:
Process the data: After downloading data (text, JSON, etc.), use Python's built-in data structures and libraries like json to manipulate it.
Error Handling: Always check for errors during requests and data retrieval using try...except blocks.