#!/usr/bin/python3
# Sends POST request with passed arg as parameter

if __name__ == "__main__":
    import requests
    from sys import argv, exit

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) <= 1:
        value = ""
    else:
        value = argv[1]

    r = requests.post(url, data={'q': value})

    try:
        obj = r.json()
        if len(obj) == 0:
            print('No result')
            exit()
        print('[{}] {}'.format(obj.get('id'), obj.get('name')))
    except ValueError:
        print('Not a valid JSON')
