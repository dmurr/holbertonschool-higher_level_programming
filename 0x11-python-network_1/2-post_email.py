#!/usr/bin/python3
# Takes in url and email as args. Sends POST and displays decoded body

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    email = argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        b = response.read()

    print(b.decode('utf-8'))
