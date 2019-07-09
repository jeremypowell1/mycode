#! /usr/bin/python3

import urllib.request
import json
import webbrowser
from pprint import pprint as pp

# Define APOD
NASAAPI = 'https://api.nasa.gov/planetary/apod?'
MYKEY = 'api_key=qLzmA3O1fFgAAezhhtwg1rrTsdM34mLbNs60Qyi6'

def main():
    """ run time code """
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY)
    nasaread = nasaapiobj.read()
    convertedjson = json.loads(nasaread.decode('utf-8'))

    print(convertedjson)
    input('\nThis is converted json. Press ENTER to continue. ')

    pp(convertedjson)
    input('\nThis is pretty printed JSON. Press ENTER to continue.')

    print(convertedjson['explanation'])
    input('\nPress ENTER to view the photo of the day')

    webbrowser.open(convertedjson['hdurl'])

main()
