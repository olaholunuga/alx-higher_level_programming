#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as result:
            print(result.read().decode("utf-8"))
    except error.HTTPError as er:
        print('Error code:', er.code)
