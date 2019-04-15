#!/usr/bin/python3
# fetches a url and displays formatted body response info

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        b = response.read()

    print('''Body response:
    - type: {}
    - content: {}
    - utf8 content: {}'''.format(type(b), b, b.decode('utf-8')))
