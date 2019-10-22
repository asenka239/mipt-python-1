import turtle

turtle.shape('turtle')


def polygon(angle, l):
    for i in range(angle):
        turtle.forward(l)
        turtle.left(360 / angle)


polygon(4, 50)
