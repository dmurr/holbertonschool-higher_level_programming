#!/usr/bin/python3
# Takes url as arg, Sends request while managing errors

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            b = response.read()
        print(b.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
