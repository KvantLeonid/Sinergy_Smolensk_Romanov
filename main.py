from turtle import *

tracer(0)
left(90)

down()
right(315)
for _ in range(7):
    forward(16 * 10)
    right(45)
    forward(8 * 10)
    right(135)
for x in range(-15, 15):
    for y in range(0, 25):
        up()
        goto(x * 10, y * 10)
        down()
        dot(3)
update()