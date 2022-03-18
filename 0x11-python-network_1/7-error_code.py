#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys

    result = requests.get(sys.argv[1])
    if (result.status_code >= 400):
        print('Error code:', result.status_code)
    else:
        print(result.text)
