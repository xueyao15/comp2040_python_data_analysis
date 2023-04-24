"""
* Assignment 8
* Xueyao Wang
* Where is the Space Station
* Sample output:
    People in Space:  10
    Sergey Prokopyev in ISS
    Dmitry Petelin in ISS
    Frank Rubio in ISS
    Nicole Mann in ISS
    Josh Cassada in ISS
    Koichi Wakata in ISS
    Anna Kikina in ISS
    Fei Junlong in Shenzhou 15
    Deng Qingming in Shenzhou 15
    Zhang Lu in Shenzhou 15
    Latitude:  36.8655
    Longitude:  -127.2677

"""
import json
import turtle
import urllib.request

# call the web service and load the data into a variable
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
astros = json.loads(response.read())

# look up the number of people in space and print it
print('People in Space: ', astros['number'])

# look up the name of the astronauts and the craft they are on
people = astros['people']
for p in people:
    print(p['name'], 'in', p['craft'])

# call the web service and get the current location of th ISS
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
iss_now = json.loads(response.read())

# create variables to store the latitude and longitude
location = iss_now['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

# set the screen size to match the size of the image
screen = turtle.Screen()
screen.setup(720, 360)
# set the screen to match the coordinates we're using
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.png')
# create a turtle icon for ISS
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
# latitude is nornally given first, but we need to give
# longitude first when plotting(x,y) coorfinates.
iss.goto(lon, lat)

# output on screen
num_people = turtle.Turtle()
num_people.penup()
num_people.hideturtle()
num_people.color('GreenYellow')
num_people.goto(-175, -25)
num_people.write('people in space: ' +
                 str(astros['number']), font=('Courier', 12, 'bold'))

turtle.exitonclick()
