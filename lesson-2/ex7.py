import turtle

turtle.shape('turtle')

def spiral (angle, l, acc):
    for i in range(acc):
        turtle.forward(l+0.05*i)
        turtle.right(360/angle)


spiral(50, 0.5, 300)  #первая и вторая переменные (их соотношение) задает ширину и размер спирали