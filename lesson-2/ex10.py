import turtle

turtle.shape('turtle')
turtle.speed(60)


def polygon(angle, l):
    for i in range(angle):
        turtle.forward(l)
        turtle.left(360 / angle)


def cir():
    polygon(500, 1)


p = int(input())

for i in range(p):
    cir()
    turtle.left(360 / p)
