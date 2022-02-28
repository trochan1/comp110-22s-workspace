"""Turtle art tutorial!"""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.pencolor("pink")
leo.fillcolor(32, 67, 98)

leo.penup()
leo.goto(-160, -100)
leo.pendown()

leo.speed(50)

side_length: int = 300

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()

bob.pencolor("orange")
bob.fillcolor(0, 0, 0)

bob.penup()
bob.goto(-160, -100)
bob.pendown()

bob.speed(100)

i: int = 0
while (i < 50):
    bob.forward(side_length * 0.97)
    bob.left(122)
    i = i + 1

done()