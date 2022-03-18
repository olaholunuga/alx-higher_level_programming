#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests

    result = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(result.text)))
    print('\t- content: {}'.format(result.text))
