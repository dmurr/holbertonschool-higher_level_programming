#!/usr/bin/python3
# Takes in url, sends request and displays value of X-Request-Id

if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers['X-Request-Id'])
