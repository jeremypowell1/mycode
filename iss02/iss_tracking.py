#! /usr/bin/python3

import urllib.request
import json
import turtle
import time

# Trace the ISS - earth oribital space station

eoss = 'http://api.open-notify.org/iss-now.json'

# Call the webserver
trackiss = urllib.request.urlopen(eoss)

# put it into a file object
ztrack = trackiss.read()

# json 2 python data structure
result = json.loads(ztrack.decode('utf-8'))

# Display the data pythonically
print("\n\nConverted python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('\nLongitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)

screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('iss_map.gif')

screen.register_shape('spriteiss.gif')
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

lon = round(float(lon))
lat = round(float(lat))
iss.penup()
iss.goto(lon, lat)

# My location
# Ask user for their latitude and longitude
yellowlat = input('Input your latitude: ')
yellowlon = input('Input your longitude: ')
yellowlat = round(float(yellowlat))
yellowlon = round(float(yellowlon))
#yellowlat = 39.0113
#yellowlon = -77.4680
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(5)
mylocation.hideturtle()

passiss = 'http://api.open-notify.org/iss-pass.json'
passiss = passiss + '?lat=' + str(yellowlat) + '&lon=' + str(yellowlon)
response = urllib.request.urlopen(passiss)
result = json.loads(response.read().decode('utf-8'))

over = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
mylocation.write(time.ctime(over), font=style)

turtle.mainloop()
