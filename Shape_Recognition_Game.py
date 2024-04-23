# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:06:23 2024

@author: Alwin
"""
import turtle as tu

# Set up the screen
wn = tu.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Disable automatic screen updates

# Create a turtle
t = tu.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(3)

# Draw a circle
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

# Ask the user for input
fq = input("What shape is this? - ").lower()
while fq != "circle":
    print("That's not the right shape.")
    fq = input("What shape is this? - ").lower()
print("Good job!")

# Manually update the screen
wn.update()
# Clear the screen for the next question
t.clear()

# Draw a square
t.penup()
t.goto(-50, -50)
t.pendown()
for _ in range(4):
    t.forward(100)
    t.right(90)

# Manually update the screen
wn.update()

# Ask the user for input
sq = input("What shape is this? - ").lower()
while sq != "square":
    print("That's not the right shape.")
    sq = input("What shape is this? - ").lower()
print("Good job!")

# Keep the window open until manually closed
tu.done()

