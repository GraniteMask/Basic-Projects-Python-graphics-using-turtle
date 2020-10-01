import turtle
import math

ratna=turtle.Turtle()
ratna.color("red")
ratna.speed(100)

for i in range(2000):
    ratna.forward(10)
    ratna.left(math.sin(i/10)*25)
    ratna.left(20)

turtle.done()
