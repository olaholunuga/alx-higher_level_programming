#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib
    
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as request:
        content = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8-content: {}".format(content.decode("utf-8")))
