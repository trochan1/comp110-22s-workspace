"""Turtle art practice!"""

from turtle import Turtle, colormode, done
snowy_ground: Turtle = Turtle()
colormode(255)

snowy_ground.pencolor(209, 209, 209)
snowy_ground.fillcolor(255, 255, 255)
snowy_ground.penup()
snowy_ground.goto(-360, -360)
snowy_ground.pendown()
snowy_ground.speed(50)
snowy_ground.begin_fill()
i: int = 0
while (i < 2):
    snowy_ground.forward(720)
    snowy_ground.left(90)
    snowy_ground.forward(175)
    snowy_ground.left(90)
    i = i + 1
snowy_ground.end_fill()
done()