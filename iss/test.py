#! /usr/bin/python3

"""Alta3| Tracking ISS"""

import urllib.request
import json

## URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    # Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    # put fileobject into helmet
    helmet = groundctrl.read()
    # Decode json to python data structure
    helmetson = json.loads(helmet.decode('utf-8'))
    # Display pythonic data
    #print("\n\nConverted Python data")
    #print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    #print(people)

    for x in people:
        print(x.get('name') + " on the " + x.get('craft'))

main()
