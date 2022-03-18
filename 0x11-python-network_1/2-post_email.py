#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    import urllib

    e_mail = urllib.parse.urlencode({"email: sys.argv[2]"}).encode()
    re_quest = urllib.request.Request(sys.argv[1], data=e_mail)
    with urllib.request.urlopen(re_quest) as result:
        print(result.read.decode("utf-8"))
