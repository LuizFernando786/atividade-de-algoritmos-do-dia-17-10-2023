#1) Mude/defina a forma da tartaruga
#2) Mude a ordem das cores#3) Mude a largura da linha
#4) Faça a tartaruga desenhar dois quadrado


import turtle

luiz = turtle.Turtle()
luiz.pensize(5)

def quadrado(tam):
    luiz.circle(tam)
for color in ['blue', 'black', 'red', 'pink']:
    luiz.color(color)
    luiz.forward(200)
    luiz.right(90)
luiz.penup()
luiz.backward(300)
luiz.pendown()

def quadrado(tam):
    luiz.circle(tam)
for color in ['black', 'blue', 'pink', 'red']:
    luiz.color(color)
    luiz.forward(200)
    luiz.right(90)
luiz.penup()
luiz.backward(300)
luiz.pendown()
