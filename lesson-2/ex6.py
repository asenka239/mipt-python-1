import turtle

turtle.shape('turtle')


def spider(paw, l):
    for i in range(paw):
        turtle.forward(l)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(l)
        turtle.right(180)
        turtle.left(360 / paw)


spider(int(input()), 50)
