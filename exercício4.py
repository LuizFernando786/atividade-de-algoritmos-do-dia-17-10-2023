import turtle
import random

luiz = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'black', 'pink']
for _ in [1, 2, 3]:
    color = random.choice(colors)
    luiz.color(color)
    luiz.forward(100)
    luiz.left(120)