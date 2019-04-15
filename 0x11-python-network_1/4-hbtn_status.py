#!/usr/bin/python3
# fetches url using requests package

if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print('''Body response:
    - type: {}
    - content: {}'''.format(r.encoding, r.text))
