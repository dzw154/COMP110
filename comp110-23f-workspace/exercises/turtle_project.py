"""Randomized Turtle Drawing: NEEDS PYTHON 3.12 TO RUN."""

__author__ = "739677774"

from turtle import Turtle, colormode, done 
import random

colormode(255)


def draw_polygon(a_turtle: Turtle, x_pos: float, y_pos: float, num_sides: float, length: float) -> None:
    """Makes the turtle draw a polygon with num_sides sides starting at the point (x_pos, y_pos)."""
    a_turtle.teleport(x_pos, y_pos)
    count: int = 0
    angle: float = 360.0 / num_sides
    while count < num_sides:
        a_turtle.forward(length)
        a_turtle.right(angle)
        count += 1


def draw_5star(a_turtle: Turtle, x_pos: float, y_pos: float, length: float) -> None:
    """Makes the turtle draw a 5-point star starting at the point (x_pos, y_pos)."""
    a_turtle.teleport(x_pos, y_pos)
    side: int = 0
    while side < 5:
        a_turtle.forward(length)
        a_turtle.left(72)
        a_turtle.forward(length)
        a_turtle.right(144)
        side += 1
    

def draw_line(a_turtle: Turtle, x_pos1: float, y_pos1: float, x_pos2: float, y_pos2: float) -> None:
    """Makes the turtle draw a line starting from point (x_pos1, y_pos1) to point (x_pos2, y_pos2)."""
    a_turtle.teleport(x_pos1, y_pos1)
    a_turtle.goto(x_pos2, y_pos2)


def draw_ellipse(a_turtle: Turtle, x_pos: float, y_pos: float, x_rad: float, y_rad: float) -> None:
    """Makes the turtle draw an ellipse starting at the point (x_pos, y_pos)."""
    a_turtle.teleport(x_pos, y_pos)
    count: int = 0
    while count < 2:
        a_turtle.circle(x_rad, 90)
        a_turtle.circle(y_rad, 90)
        count += 1


def rand_pen_color(a_turtle: Turtle) -> None:
    """Sets the turtle's pen color to a random RGB value."""
    a_turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def rand_speed(a_turtle: Turtle) -> None:
    """Sets the turtle's speed to a random value from 0 to 10 inclusive."""
    a_turtle.speed(random.randint(0, 10))


def rand_fill(a_turtle: Turtle) -> None:
    """Sets the turtle's fill color to a random RGB value."""
    a_turtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def rand_heading(a_turtle: Turtle) -> None:
    """Sets the turtle's heading to a random direction."""
    a_turtle.setheading(random.randint(0, 360))


def main() -> None:
    """Creates a turtle object futa that will draw 100 shapes and lines in a variety of colors at a variety of speeds."""
    futa: Turtle = Turtle()
    counter: int = 0
    while counter < 100:
        draw_what: int = random.randint(0, 4)
        pen_what: int = random.randint(0, 4)
        fill_status: int = random.randint(0, 20)
        if fill_status < 11:
            futa.begin_fill()
        if fill_status > 11:
            futa.end_fill()
        
        if pen_what == 0:
            rand_pen_color(futa)
        if pen_what == 1:
            rand_fill(futa)
        if pen_what == 2:
            rand_heading(futa)
        if pen_what == 3:
            rand_speed(futa)
        if draw_what == 0:
            draw_polygon(futa, random.uniform(-400, 400), random.uniform(-400, 400), random.randint(3, 20), random.randint(1, 50))
        
        if draw_what == 1:
            draw_5star(futa, random.uniform(-400, 400), random.uniform(-400, 400), random.randint(1, 50))

        if draw_what == 2:
            draw_ellipse(futa, random.uniform(-400, 400), random.uniform(-400, 400), random.randint(1, 50), random.randint(1, 50))

        if draw_what == 3:
            draw_line(futa, random.uniform(-400, 400), random.uniform(-400, 400), random.uniform(-400, 400), random.uniform(-400, 400))
        counter += 1
    done()


if __name__ == "__main__":
    main()