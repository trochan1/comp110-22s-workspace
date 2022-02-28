"""EX04 - Turtle Scene Exercise - Little turtle friends paint a snowy scene!"""

__author__ = "730489697"


from turtle import Turtle, colormode, done
colormode(255)
# I added colormode(255) to enable RGB mode, which allows me to make my own colors by adding certain amounts
# of red, green, and blue!

def draw_sky(sky: Turtle, x: float, y: float) -> None:
    """Paints the sky."""
    sky.pencolor(20, 106, 154)
    sky.fillcolor(20, 106, 154)
    sky.penup()
    sky.goto(x, y)
    sky.pendown()
    sky.speed(50)
    sky.begin_fill()
    i: int = 0
    while (i < 4):
    # This while loop draws a square with side lengths of 720.
        sky.forward(720)
        sky.left(90)
        i = i + 1
    sky.end_fill()

def draw_snowy_ground(snow: Turtle, x: float, y: float) -> None:
    """Paints the snowy ground."""
    snow.pencolor(209, 209, 209)
    snow.fillcolor(240, 240, 240)
    snow.penup()
    snow.goto(x, y)
    snow.pendown()
    snow.speed(50)
    snow.begin_fill()
    i: int = 0
    while (i < 2):
    # This while loop draws a rectangle with side lengths of 720 and 175. Since all four side lengths are not equal,
    # I could not use the same method with the index i as I did with the square.
        snow.forward(720)
        snow.left(90)
        snow.forward(175)
        snow.left(90)
        i = i + 1
    snow.end_fill()

def draw_snowflakes(snowflakes: Turtle, x: float, y: float) -> None:
    """Fills the sky with beautiful snowflakes."""
    snowflakes.pencolor(255, 255, 255)
    snowflakes.penup()
    snowflakes.goto(x, y)
    snowflakes.pendown()
    snowflakes.speed(100)
    i: int = 0
    while (i < 6):
        snowflakes.forward(10)
        snowflakes.left(180)
        snowflakes.forward(10)
        snowflakes.left(25)
        # I chose 25 degrees because I liked how it made the snowflakes look unique and uneven.
        i = i + 1

def draw_snowman(snowman: Turtle, x: float, y: float, radius: float) -> None:
    """Draws the snowballs that help to build two cute snowpeople! A fourth parameter (radius) was added to manipulate the size of each snowball."""
    snowman.pencolor(128, 128, 128)
    snowman.fillcolor(240, 240, 240)
    snowman.penup()
    snowman.goto(x, y)
    snowman.pendown()
    snowman.speed(50)
    snowman.begin_fill()
    snowman.circle(radius)
    # I added a fourth parameter for radius so that I could manipulate the size of each snowball later on within my main function.
    snowman.end_fill()

def draw_heart(heart: Turtle, x: float, y: float) -> None:
    """Draws a heart to show the snowpeoples' love for eachother!"""
    heart.pencolor(214, 132, 217)
    heart.fillcolor(240, 180, 242)
    heart.penup()
    heart.goto(x, y)
    heart.pendown()
    heart.speed(50)
    heart.right(30)
    # I had to rotate my turtle to the right by 30 degrees prior to actually drawing the heart because it was 
    # looking oddly tilted to the left before.
    def heart_shape() -> None:
        """Tells the turtle the specific directions for how to paint a heart shape."""
        # I tried something fun by experimenting with how to make a heart!
        heart.left(60)
        heart.forward(150)
        heart.circle(40, 200)
        heart.right(160)
        heart.circle(40, 200)
        heart.forward(150)
    heart.begin_fill()
    heart_shape()
    heart.end_fill()

def draw_eye(eye: Turtle, x: float, y: float) -> None:
    """Adds eyes to both snowmen!"""
    eye.pencolor(5, 5, 5)
    eye.fillcolor(5, 5, 5)
    eye.penup()
    eye.goto(x, y)
    eye.pendown()
    eye.speed(50)
    eye.begin_fill()
    eye.circle(2)
    eye.end_fill()
    eye.hideturtle()
    # I added the hideturtle at the end of the draw_eye function because this is the last function called by the main function.

def main() -> None:
    """Commands the little turtle friends to start painting!"""
    turtles: Turtle = Turtle()
    draw_sky(turtles, -360, -360)
    draw_snowy_ground(turtles, -360, -360)
    draw_snowflakes(turtles, -300, 150)
    draw_snowflakes(turtles, -150, 300)
    draw_snowflakes(turtles, 0, 100)
    draw_snowflakes(turtles, 150, 300)
    draw_snowflakes(turtles, 300, 150)
    draw_snowman(turtles, -90, -185, 90)
    # I could manipulate the radius in the fourth parameter of the draw_snowman function.
    draw_snowman(turtles, -90, -65, 70)
    draw_snowman(turtles, -90, 55, 50)
    draw_snowman(turtles, 125, -185, 90)
    draw_snowman(turtles, 105, -65, 70)
    draw_snowman(turtles, 85, 55, 50)
    draw_heart(turtles, -25, 130)
    draw_eye(turtles, -100, 90)
    draw_eye(turtles, -90, 90)
    draw_eye(turtles, 35, 90)
    draw_eye(turtles, 45, 90)
    done()

if __name__ == "__main__":
    main()