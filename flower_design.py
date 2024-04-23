# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:54:19 2024

@author: Alwin
"""

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)
t.color("red", "yellow")
t.begin_fill()

# Draw the flower petals
for _ in range(36):
    t.forward(200)
    t.left(170)

# End the fill
t.end_fill()

# Hide the turtle and display the result
t.hideturtle()

# Close the turtle graphics window when clicked
screen.exitonclick()
