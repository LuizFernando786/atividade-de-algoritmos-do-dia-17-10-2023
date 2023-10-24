#1) Mude a distancia entre as lentes dos óculos
#2) Mude o tamanho das lentes

import turtle

luiz = turtle.Turtle()
luiz.color('green')

for _ in range(4):
    luiz.left(90)
    luiz.backward(60)

luiz.backward(50)
luiz.backward(90)
luiz.right(90)

for _ in range(3):
  luiz.forward(60)
  luiz.left(90)