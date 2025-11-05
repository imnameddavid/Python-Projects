#3

import turtle

shape = int(input("How many sides shape would you like? ")) 
tcolor = input("Choose a color: ")
width = input("Choose your width: ")

t = turtle.Turtle()
t.shape("arrow")
t.color(tcolor)
t.width(width)
t.speed(10)

for i in range(shape):
    t.forward(1000 / shape)
    t.right(360 / shape)
turtle.done()