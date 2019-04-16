#!/usr/bin/python3
# Takes in a string and sends a search request to the Star Wars API

if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://swapi.co/api/people/'

    r = requests.get(url, params={'search': argv[1]})

    obj = r.json()
    print('Number of results: {}'.format(obj['count']))
    results = obj.get('results')
    for d in results:
        print(d.get('name'))
