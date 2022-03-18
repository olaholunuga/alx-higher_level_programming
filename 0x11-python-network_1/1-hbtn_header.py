#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id
"""

if __name__ == "__main__":
    import sys
    import urllib

    with urllib.request.urlopen(sys.argv[1]) as request:
        print(request.info()["X-Request-Id"])
