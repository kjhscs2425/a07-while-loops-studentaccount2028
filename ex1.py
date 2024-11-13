# Use turtle graphics to make an infinite spiral
import turtle
turtle.speed(100000000)
length = 1
while True:
    turtle.forward(length)
    turtle.left(10)
    length +=0.1