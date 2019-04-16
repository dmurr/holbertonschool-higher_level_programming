#!/usr/bin/python3
# fetches a url and displays formatted body response info

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        b = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(b)))
        print("\t- content: {}".format(b))
        print("\t- utf8 content: {}".format(b.decode("utf-8")))
