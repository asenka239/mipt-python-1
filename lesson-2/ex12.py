import turtle

turtle.shape('turtle')
turtle.speed(60)


def semipolygon(angle, l):
    for i in range(angle // 2):
        turtle.forward(l)
        turtle.right(360 / angle)


big = int(input())
sm = int(input())
n = int(input())

turtle.left(90)
for i in range(n):
    semipolygon(big, 1)
    semipolygon(sm, 1)
