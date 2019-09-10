import turtle

turtle.shape('turtle')
turtle.speed(60)

def polygon (angle, l):
    for i in range(angle):
        turtle.forward(l)
        turtle.left(360/angle)
def semisemipolygonR (angle, l):
    for i in range(angle//4):
        turtle.forward(l)
        turtle.right(360/angle) 
def semisemipolygonL (angle, l):
    for i in range(angle//4):
        turtle.forward(l)
        turtle.left(360/angle)                
def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

goto(0, -100)
turtle.begin_fill()
polygon(250, 2)
turtle.color('yellow')
turtle.end_fill()
turtle.color('black')

goto(-30, -5)

turtle.begin_fill()
polygon(50, 2)
turtle.color('purple')
turtle.end_fill()
turtle.color('black')


goto(30, -5)

turtle.begin_fill()
polygon(50, 2)
turtle.color('purple')
turtle.end_fill()
turtle.color('black')

goto(0, 0)
turtle.right(90)
turtle.width(8)
turtle.color('purple')
turtle.forward(20)

goto(0, -70)
turtle.right(90)
turtle.width(8)
turtle.color('purple')
semisemipolygonR(200, 1)


goto(0, -70)
turtle.right(90)
turtle.width(8)
turtle.color('purple')
semisemipolygonL(200, 1)




k = input()


