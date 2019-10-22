import turtle

turtle.shape('turtle')
turtle.speed(60)


def polygon(angle, l):
    for i in range(angle):
        turtle.forward(l)
        turtle.left(360 / angle)
    for i in range(angle):
        turtle.forward(l)
        turtle.right(360 / angle)


turtle.left(90)
for j in range(int(input())):
    polygon(100 + j * 25, 1)
