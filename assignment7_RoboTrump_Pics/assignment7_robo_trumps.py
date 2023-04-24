"""
* Assignment 7
* Xueyao Wang
* Robo Trumps
* Sample output:
    Robots: rainbow, space, bird, jet, brains, tv, yellow, dog, shades (or random)
    Choose a robot: rainbow
    Choose a robot: space
    Choose a robot: random
    tv

"""

from random import choice
from turtle import *

screen = Screen()
screen.bgcolor('white')
penup()
hideturtle()

robots = {}

# file = open('cards.txt', 'r')
with open('cards.txt', 'r') as file:
    for line in file.read().splitlines():
        name, battery, intelligence, usefulness, fastness, colors, image = line.split(', ')
        robots[name] = [battery, intelligence, usefulness, fastness, colors, image]
        screen.register_shape(image)

# file.close()

print('Robots: rainbow, space, bird, jet, brains, tv, yellow, dog, shades (or random)')


while True:
    robot = input('Choose a robot or enter E to exit: ')

    if robot == 'random':
        robot = choice(list(robots.keys()))
        print(robot)
    if robot in robots:
        stats = robots[robot]
        style = ('Arial', 14, 'bold')
        clear()
        goto(0, 100)
        shape(stats[5])
        setheading(90)
        stamp()
        setheading(-90)
        forward(70)
        color(stats[4])
        write('Name: ' + robot, font=style, align='center')
        forward(25)
        write('Battery: ' + stats[0], font=style, align='center')
        forward(25)
        write('Intelligence: ' + stats[1], font=style, align='center')
        forward(25)
        write('Usefulness: ' + stats[2], font=style, align='center')
        forward(25)
        write('Fastness: ' + stats[3], font=style, align='center')
    elif robot == 'E':
        break
    else:
        print('Robot doesn\'t exist!')
