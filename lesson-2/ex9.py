import turtle
import math

turtle.shape('turtle')


def polygon(angle, l, k, rx):
    r = l / (2 * math.sin(2 * math.pi / (2 * angle)))
    for j in range(k):
        turtle.right(90 - 90 * (angle - 2) / angle)
        for i in range(angle):
            turtle.forward(l)
            turtle.right(360 / angle)
        turtle.left(90 - 90 * (angle - 2) / angle)
        turtle.left(90)
        turtle.penup()
        turtle.forward(rx)
        turtle.pendown()
        turtle.right(90)
        angle += 1
        r += rx
        l = r * (2 * math.sin(2 * math.pi / (2 * angle)))


polygon(3, 10, 10, 5)
