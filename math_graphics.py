import turtle
import math

ratna=turtle.Turtle()
ratna.color("red")
ratna.speed(10)

for i in range(2000):
    ratna.forward(math.sqrt(i))
    ratna.left(i%180)

turtle.done()
