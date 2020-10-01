#star graphics
import turtle

ratna=turtle.Turtle()
ratna.color('red', 'yellow')
ratna.speed(100)
ratna.begin_fill()
while True:
    ratna.forward(200)
    ratna.left(170)
    if abs(ratna.pos()) < 1:
        break
ratna.end_fill()

ratna.penup()
ratna.left(200)
ratna.pendown()

ratna.color('blue', 'red')
ratna.begin_fill()
for i in range(200):
    ratna.forward(300)
    ratna.left(170)
ratna.end_fill()
turtle.done()

#both part of the code has the same function
