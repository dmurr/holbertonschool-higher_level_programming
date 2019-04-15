#!/usr/bin/python3
# Takes url argument, sends request, and displays value of X-Request-Id

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        info = response.info()

    print(info['X-Request-Id'])
