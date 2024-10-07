import turtle
import random

# Function to draw a dot with given color at a random position
def draw_dot(color):
    turtle.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.goto(x, y)
    turtle.dot(20, color)

# Main function to draw N red dots and N green dots
def draw_dots(N):
    turtle.speed(0)  # Set the fastest drawing speed
    for _ in range(N):
        draw_dot('red')
    for _ in range(N):
        draw_dot('green')

# Setup the screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor("white")

# Call the main function with the number of dots you want
draw_dots(5)

# Keep the window open
turtle.done()
