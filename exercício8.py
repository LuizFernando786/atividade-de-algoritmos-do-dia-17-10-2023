#1) Adicione núcleos
#2) Mudar a largura da linha
#3) Aumente a quantidade de linhas

import turtle
import random

turtle = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink']
for _ in range (18):
    color = random.choice(colors)
    turtle.color(color)
    turtle.right(50)
    turtle.forward(200)
    turtle.backward(200)
    turtle.right(45)