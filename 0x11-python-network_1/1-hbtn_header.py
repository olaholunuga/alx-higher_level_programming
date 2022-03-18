#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info()["X-Request-Id"])
