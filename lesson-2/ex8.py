import turtle

turtle.shape('turtle')

def spiralq(l, r, acc): #сторона первого, шаг, количество витков
    for i in range(acc):
        for j in range(4):
            turtle.forward(l+r*(i*4+j))
            turtle.left(90)

spiralq(5, 2, 10)