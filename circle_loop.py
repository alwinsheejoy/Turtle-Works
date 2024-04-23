# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:21:05 2024

@author: Alwin
"""

import turtle as tu

colors = ["gold", "silver","red"]
wn = tu.Screen()
wn.bgcolor("black")
t = tu.Turtle()
t.speed(0)
t.pensize(3)

# Draw a spiral pattern
for x in range(250):
    t.pencolor(colors[x % 2])
    t.width(x / 5 + 1)
    t.forward(x)
    t.right(45)
    t.circle(x)


tu.done()
