import turtle

turtle.shape('turtle')
turtle.speed(60)


def star(angle, l):
    for i in range(angle):
        turtle.forward(l)
        turtle.right(180 - 180 / angle)


angle = int(input())

l = int(input())

star(angle, l)

k = input()  # чтобы посмотреть успеть
