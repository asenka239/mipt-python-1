import turtle

turtle.shape('turtle')


def polygon(angle, l, k, r):
    for j in range(k):
        for i in range(angle):
            turtle.forward(l + 2 * j * r)
            turtle.left(360 / angle)
        turtle.penup()
        turtle.right(360 / angle)
        turtle.forward(r)
        turtle.right(360 / angle)
        turtle.forward(r)
        turtle.left(360 / angle)
        turtle.left(360 / angle)
        turtle.pendown()


polygon(4, 5, 10, 5)
