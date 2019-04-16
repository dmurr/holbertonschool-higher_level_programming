#!/usr/bin/python3
# Sends POST request to url and passes email. Displays body of response

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
