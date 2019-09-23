from graph import *
import math

windowSize(600, 800)
canvasSize(600, 800)



def oval(a, b, x0, y0, c = 100):
    mass = list()

    for alpha_c in range(0, c):
        alpha = alpha_c / c * 2 * math.pi
        mass.append((x0 + a * math.cos(alpha), y0 + b * math.sin(alpha)))

    polygon(mass)

penColor(136, 236, 255)
brushColor(136, 236, 255)
rectangle(0, 0, 600, 400) #sky

penColor(68, 255, 74)
brushColor(68, 255, 74)
rectangle(0, 400, 600, 800) #ground

def sun():
    brushColor(254, 254, 34)
    penColor(254, 254, 34)
    circle(570, 30, 60) #sun

    #rays of sunshine

    penColor(254, 254, 34) 
    brushColor(254, 254, 34)
    polygon([(535,  7), (540, 37), (465, 25)]) 
    polygon([(565, 10), (585, 60), (490, 100)])
    polygon([(565, 80), (587, 85), (575, 130)])

def colorStuff(color, stuff, *argv):
    if type(color) == type('string'):
        brushColor(color)
        penColor(color)
    else:
        brushColor(color[0], color[1], color[2])
        penColor(color[0], color[1], color[2])

    stuff(*argv)

def tree(trunk, crown, apple):
    brushColor(trunk)
    penColor(trunk)
    rectangle(50+45, 300, 75+55, 550) #tree trunk(ствол)

    #from here --- tree crown

    colorStuff(crown, circle, 70+50, 200, 70)
    colorStuff(crown, circle, -20+50, 250, 70)
    colorStuff(crown, circle, 70+50, 250, 70)
    colorStuff(crown, circle, 130+50, 240, 70)
    colorStuff(crown, circle, -20+50, 290, 70)
    colorStuff(crown, circle, 70+50, 300, 70)
    colorStuff(crown, circle, 130+50, 300, 70)
    colorStuff(crown, circle, 170+50, 300, 70)

    #apples

    penColor(apple) 
    brushColor(apple)

    for i in range(6):
        if(i != 0):
            circle(170 + 17 * i * (-1) ** (i), 200 + 27 * i , 15 + 2 * (-1) ** (i))

    circle(75+50, 160, 13)
    circle(128+50, 330, 15)
    circle(40+50, 189, 18)
    circle(28+50, 250, 15)
    circle(32, 220, 12)
    circle(17, 296, 16)

def unicorn(leg, hoof, body, horn, tail, mane): 
    """In tail >= 4 elements, in mane >= 5 elements, body is the colour if body, neck and head. 
    Eye color is const."""

    colorStuff(leg, rectangle, 300, 500, 315, 600)
    colorStuff(hoof, rectangle, 300, 600, 315, 593) #from left to right --- 1 unicorn leg

    colorStuff(leg, rectangle, 330, 490, 342, 585)
    colorStuff(hoof, rectangle, 330, 580, 342, 587)  #from left to right --- 2 unicorn leg

    colorStuff(leg, rectangle, 380, 507, 395, 607)
    colorStuff(hoof, rectangle, 380, 602, 395, 609)  #from left to right --- 3 unicorn leg

    colorStuff(leg, rectangle, 430, 470, 442, 583)
    colorStuff(hoof, rectangle, 430, 578, 442, 585) #from left to right --- 4 unicorn leg



    colorStuff(body, oval, 100, 50, 370, 480) #unicorn body

    colorStuff(body, oval, 30, 70, 450, 430) #unicorn neck

    #horn

    colorStuff(horn, polygon, [(450, 370), (470, 370), (485, 300)])


    colorStuff(body, circle, 450, 370, 30) #unicorn head
    oval(40, 20, 480, 370) 

    

    #eye

    colorStuff((255, 227, 217), oval, 9, 7, 460, 363)
    colorStuff('black', circle, 465, 365, 2)


    #unicorn mane
    x = 430
    y = 350
    a = 15
    b = 7
    par_x = 6
    par_y = 17
    penColor('purple') 
    brushColor('purple')

    for i in range(5):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)

    penColor(mane[0]) 
    brushColor(mane[0])

    y += 20
    x -= 15

    for i in range(5):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)

    penColor(mane[1]) 
    brushColor(mane[1])


    x -= 15
    y += 20

    for i in range(4):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)

        

    penColor(mane[2]) 
    brushColor(mane[2])


    y -= 15
    x += 35
    par_y -= 3

    for i in range(5):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)



    penColor(mane[3]) 
    brushColor(mane[3])

    y -= 20
    x -= 25
    par_x -= 3

    for i in range(7):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)




    #unicorn tail
    x = 280
    y = 450
    a = 15
    b = 7
    par_x = 6
    par_y = 17
    penColor(tail[0]) 
    brushColor(tail[0])

    for i in range(7):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)

    penColor(tail[1]) 
    brushColor(tail[1])

    y += 20
    x -= 15

    for i in range(7):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)

    penColor(tail[2]) 
    brushColor(tail[2])


    x -= 15
    y += 20

    for i in range(6):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)

        

    penColor(tail[3]) 
    brushColor(tail[3])


    y -= 15
    x += 35
    par_y -= 3

    for i in range(7):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)



    penColor(tail[4]) 
    brushColor(tail[4])

    y -= 20
    x -= 25
    par_x -= 3

    for i in range(10):
        oval(a, b, x - par_x * i * (-1) ** (i), y + par_y * i)





sun()
tree((128, 64, 28), (61, 156, 51), (217, 0, 40))
unicorn('white', (184, 134, 11), 'white', (184, 134, 11), [(143, 0, 255), (205, 1, 203), (152, 18, 150), (226, 94, 240), (99, 0, 155)], [(205, 1, 203), (99, 0, 155), (152, 18, 150), (143, 0, 255), (226, 94, 240)])








   





















    






run()