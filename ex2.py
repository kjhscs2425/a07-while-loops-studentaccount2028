# make infinite circles, start with a small circle, then draw a bigger circle around it
import turtle
turtle.speed(2374897239472937492784982378492938749823748972938479823748972893748923749872893749823789498273984792374897238947892374982374987239847289374823749)
circle_len = 0.1
while True:
    for i in range(365):
        turtle.forward(circle_len)
        turtle.left(1)
    circle_len += 0.1