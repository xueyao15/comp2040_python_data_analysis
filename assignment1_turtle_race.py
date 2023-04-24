from turtle import *
from random import randint

speed(0)
penup()
goto(-140,140)

for step in range(15):
    write(step, align = 'center')
    right(90)
    for i in range(8):
        forward(10)
        pendown()
        forward(10)
        penup() 
    backward(160)
    left(90)
    forward(20)


a = Turtle()
a.color('tomato')
a.shape('turtle')

a.penup()
a.goto(-160,100)
a.pendown()


b = Turtle()
b.color('powder blue')
b.shape('turtle')

b.penup()
b.goto(-160,70)
b.pendown()

c = Turtle()
c.color('plum')
c.shape('turtle')

c.penup()
c.goto(-160,40)
c.pendown()

d = Turtle()
d.color('yellow green')
d.shape('turtle')

d.penup()
d.goto(-160,10)
d.pendown()

for turn in range(100):
    a.forward(randint(1,5))
    b.forward(randint(1,5))
    c.forward(randint(1,5))
    d.forward(randint(1,5))

for turn in range(8):
    a.right(45)
    b.right(45)
    c.right(45)
    d.right(45)

turtle.done()
