from graph import *
import math
import random


def oval(a, b, x0, y0, c=100):
    mass = list()

    for alpha_c in range(0, c):
        alpha = alpha_c / c * 2 * math.pi
        mass.append((x0 + a * math.cos(alpha), y0 + b * math.sin(alpha)))

    polyg = polygon(mass)
    return polyg


def sun():
    global allSun
    brushColor(254, 254, 34)
    penColor(254, 254, 34)
    sunCir = circle(570, 30, 60)  # sun

    # rays of sunshine
    penColor(254, 254, 34)
    brushColor(254, 254, 34)
    sunSh1 = polygon([(535,  7), (540, 37), (465, 25)])
    sunSh2 = polygon([(565, 10), (585, 60), (490, 100)])
    sunSh3 = polygon([(565, 80), (587, 85), (575, 130)])

    allSun = list()
    allSun.append(sunCir)
    allSun.append(sunSh1)
    allSun.append(sunSh2)
    allSun.append(sunSh3)


def generateCoord(count, weight, height, x0, y0):
    coord = list()
    for i in range(count):
        x = random.random() * weight + x0
        y = random.random() * height + y0
        r = random.random() * 14 + 2
        coord.append((x, y, r))
    return coord


def creatStars(coord, ang):
    global massOfStars
    massOfStars = list()
    for j in range(len(coord)):
        st = list()
        for i in range(5):
            par1 = math.pi * i * 2 / 5
            x_i = coord[j][0] + coord[j][2] * math.cos(ang - par1)
            y_i = coord[j][1] + coord[j][2] * math.sin(ang - par1)
            st.append((x_i, y_i))
            par2 = ang - math.pi * (i + 0.5) * 2 / 5
            par3 = math.cos(math.pi * 2 / 5) / math.cos(math.pi / 5)
            x_i = coord[j][0] + coord[j][2] * math.cos(par2) * par3
            y_i = coord[j][1] + coord[j][2] * math.sin(par2) * par3
            st.append((x_i, y_i))
        oneStar = polygon(st)
        massOfStars.append(oneStar)


def deleteManyObjects(objects):
    for i in range(len(objects)):
        deleteObject(objects[i])


def colorStuff(color, stuff, *argv):
    if isinstance(color, str):
        brushColor(color)
        penColor(color)
    else:
        brushColor(color[0], color[1], color[2])
        penColor(color[0], color[1], color[2])
    obj = stuff(*argv)
    return obj


def tree(trunk, crown, apple):
    global allTree
    allTree = list()
    brushColor(trunk)
    penColor(trunk)
    th = rectangle(50+45, 300, 75+55, 550)  # tree trunk(ствол)
    allTree.append(th)

    # from here --- tree crown

    cr = colorStuff(crown, circle, 70+50, 200, 70)
    allTree.append(cr)
    cr = colorStuff(crown, circle, -20+50, 250, 70)
    allTree.append(cr)
    cr = colorStuff(crown, circle, 70+50, 250, 70)
    allTree.append(cr)
    cr = colorStuff(crown, circle, 130+50, 240, 70)
    allTree.append(cr)
    cr = colorStuff(crown, circle, -20+50, 290, 70)
    allTree.append(cr)
    cr = colorStuff(crown, circle, 70+50, 300, 70)
    allTree.append(cr)
    cr = colorStuff(crown, circle, 130+50, 300, 70)
    allTree.append(cr)
    cr = colorStuff(crown, circle, 170+50, 300, 70)
    allTree.append(cr)

    # apples

    penColor(apple)
    brushColor(apple)

    for i in range(6):
        if i != 0:
            x = 170 + 17 * i * (-1) ** (i)
            y = 200 + 27 * i
            r = 15 + 2 * (-1) ** (i)
            ap = circle(x, y, r)
            allTree.append(ap)

    ap = circle(75+50, 160, 13)
    allTree.append(ap)
    ap = circle(128+50, 330, 15)
    allTree.append(ap)
    ap = circle(40+50, 189, 18)
    allTree.append(ap)
    ap = circle(28+50, 250, 15)
    allTree.append(ap)
    ap = circle(32, 220, 12)
    allTree.append(ap)
    ap = circle(17, 296, 16)
    allTree.append(ap)


def unicorn(leg, hoof, body, horn, tail, mane, axis):
    """In tail >= 5 elements, in mane >= 5 elements,
    body is the colour if body, neck and head.
    Eye color is const.
    axis"""

    global allUnicorn, tailArr, head_array
    allUnicorn = list()
    tailArr = list()
    head_array = list()

    # from left to right --- 1 unicorn leg
    leg1 = colorStuff(leg, rectangle, 300, 500, 315, 600)
    hoof1 = colorStuff(hoof, rectangle, 300, 600, 315, 593)

    # from left to right --- 2 unicorn leg
    leg2 = colorStuff(leg, rectangle, 330, 490, 342, 585)
    hoof2 = colorStuff(hoof, rectangle, 330, 580, 342, 587)

    # from left to right --- 3 unicorn leg
    leg3 = colorStuff(leg, rectangle, 380, 507, 395, 607)
    hoof3 = colorStuff(hoof, rectangle, 380, 602, 395, 609)

    # from left to right --- 4 unicorn leg
    leg4 = colorStuff(leg, rectangle, 430, 470, 442, 583)
    hoof4 = colorStuff(hoof, rectangle, 430, 578, 442, 585)

    body1 = colorStuff(body, oval, 100, 50, 370, 480)  # unicorn body

    neck = colorStuff(body, oval, 30, 70, 450, 430)  # unicorn neck

    # horn

    horn1 = colorStuff(horn, polygon, [(450, 370), (470, 370), (485, 300)])
    head1 = colorStuff(body, circle, 450, 370, 30)  # unicorn head
    head2 = oval(40, 20, 480, 370)
    
    # eye

    whitePartOfEye = colorStuff((255, 227, 217), oval, 9, 7, 460, 363)
    blackPartOfEye = colorStuff('black', circle, 465, 365, 2)

    allUnicorn.extend((leg1, hoof1, leg2, hoof2, leg3, hoof3, leg4, hoof4))
    allUnicorn.extend((body1, neck, horn1, head1, head2))
    allUnicorn.extend((whitePartOfEye, blackPartOfEye))
    
    head_array.extend((horn1, head1, head2, whitePartOfEye, blackPartOfEye))

    # unicorn mane
    random.shuffle(mane)
    random.shuffle(axis)
    x = 430
    y = 350
    par_x = 6
    par_y = 17
    penColor(mane[4])
    brushColor(mane[4])

    for i in range(5):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[4][0], axis[4][1], x_i, y_i)
        allUnicorn.append(fig)
        head_array.append(fig)

    penColor(mane[0])
    brushColor(mane[0])

    y += 20
    x -= 15

    for i in range(5):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[0][0], axis[0][1], x_i, y_i)
        allUnicorn.append(fig)
        head_array.append(fig)

    penColor(mane[1])
    brushColor(mane[1])

    x -= 15
    y += 20

    for i in range(4):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[1][0], axis[1][1], x_i, y_i)
        allUnicorn.append(fig)
        head_array.append(fig)

    penColor(mane[2])
    brushColor(mane[2])

    y -= 15
    x += 35
    par_y -= 3

    for i in range(5):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[2][0], axis[2][1], x_i, y_i)
        allUnicorn.append(fig)
        head_array.append(fig)

    penColor(mane[3])  # mane[3]
    brushColor(mane[3])

    y -= 20
    x -= 25
    par_x -= 3

    for i in range(7):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[3][0], axis[3][1], x_i, y_i)
        allUnicorn.append(fig)
        head_array.append(fig)

    penColor(mane[5])  # mane[5]
    brushColor(mane[5])

    y += 20
    x += 20
    par_y -= 2
    par_x -= 2

    for i in range(7):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[5][0], axis[5][1], x_i, y_i)
        allUnicorn.append(fig)
        head_array.append(fig)

    # unicorn tail
    random.shuffle(tail)
    random.shuffle(axis)
    x = 280
    y = 450
    par_x = 6
    par_y = 17
    penColor(tail[0])
    brushColor(tail[0])

    for i in range(7):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[0][0], axis[0][1], x_i, y_i)
        allUnicorn.append(fig)
        tailArr.append(fig)

    penColor(tail[1])
    brushColor(tail[1])

    y += 20
    x -= 15

    for i in range(7):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[1][0], axis[1][1], x_i, y_i)
        allUnicorn.append(fig)
        tail.append(fig)

    penColor(tail[2])
    brushColor(tail[2])

    x -= 15
    y += 20

    for i in range(6):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[2][0], axis[2][1], x_i, y_i)
        allUnicorn.append(fig)
        tailArr.append(fig)

    penColor(tail[3])
    brushColor(tail[3])

    y -= 15
    x += 35
    par_y -= 3

    for i in range(7):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[3][0], axis[3][1], x_i, y_i)
        allUnicorn.append(fig)
        tailArr.append(fig)

    penColor(tail[4])  # tail[4]
    brushColor(tail[4])

    y -= 20
    x -= 25
    par_x -= 3

    for i in range(10):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[4][0], axis[4][1], x_i, y_i)
        allUnicorn.append(fig)
        tailArr.append(fig)

    penColor(tail[5])  # tail[5]
    brushColor(tail[5])

    y += 37
    x += 23
    par_x -= 1
    par_y -= 1

    for i in range(7):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[5][0], axis[5][1], x_i, y_i)
        allUnicorn.append(fig)
        tailArr.append(fig)

    penColor(tail[6])  # tail[6]
    brushColor(tail[6])

    y += 37
    x -= 40

    for i in range(5):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[6][0], axis[6][1], x_i, y_i)
        allUnicorn.append(fig)
        tailArr.append(fig)

    y -= 37
    x += 40

    penColor(tail[5])  # tail[5]
    brushColor(tail[5])

    for i in range(7):
        x_i = x - par_x * i * (-1) ** (i)
        y_i = y + par_y * i
        fig = oval(axis[5][0], axis[5][1], x_i, y_i)
        allUnicorn.append(fig)
        tailArr.append(fig)


def dayNight():
    global flag
    if flag:
        changeProperty(sky, fill='blue4', outline='blue4')
        changeProperty(ground, fill='chartreuse4', outline='chartreuse4')
        deleteManyObjects(allSun)
        penColor('yellow')
        brushColor('yellow')
        coord = generateCoord(50, 600, 350, 0, 0)
        creatStars(coord, 0)
        deleteManyObjects(allTree)
        tree((128, 64, 28), 'dark green', (217, 0, 40))
#       mane = [(49, 0, 98), (192, 5, 218), (182, 39, 246)]
#       mane.extend(((172, 73, 245), (191, 5, 247), (149, 33, 246)))
#       mane.extend(((143, 0, 255), (205, 1, 203), (152, 18, 150)))
#       mane.extend(((226, 94, 240), (99, 0, 155)))
#       tail = [(49, 0, 98), (192, 5, 218), (182, 39, 246)]
#       tail.extend(((172, 73, 245), (191, 5, 247), (149, 33, 246)))
#       tail.extend(((143, 0, 255), (205, 1, 203), (152, 18, 150)))
#       tail.extend(((226, 94, 240), (99, 0, 155)))
        axis = generateCoord(10, 17, 9, 10, 8)
        for unic in allUnicorn:
            canvas().tag_raise(unic)
    else:
        changeProperty(sky, fill='deep sky blue', outline='deep sky blue')
        changeProperty(ground, fill='DarkOliveGreen1', outline='DarkOliveGreen1')
        deleteManyObjects(allTree)
        tree((128, 64, 28), 'forest green', (217, 0, 40))
        deleteManyObjects(massOfStars)
        sun()
        for unic in allUnicorn:
            canvas().tag_raise(unic)
    flag = not flag


jump_height = 25

jump_dy = 0
up_jump = True
def jump():
    global jump_dy, up_jump
    rand_x = 0#int(random.random()*6)-3
    if up_jump:
        for i in allUnicorn:
            moveObjectBy(i, rand_x, 1)
        jump_dy += 1
    else:
        for i in allUnicorn:
            moveObjectBy(i, rand_x, -1)
        jump_dy -= 1
    if jump_dy <= 0:
        up_jump = True
    elif jump_dy >= jump_height:
        up_jump = False
       
dx = 0
maxim_x = int(random.random()*7)
right_tail = True
def wind():
    global dx, maxim_x, right_tail
    if right_tail: 
        for i in tailArr:
            moveObjectBy(i, 1, 0)
        dx += 1    
    else:
        for i in tailArr:
            moveObjectBy(i, -1, 0)
        dx -= 1
    if right_tail and dx >= maxim_x:
        right_tail = False
        maxim_x = int(random.random()*7)
    elif (not right_tail) and dx <= -maxim_x:
        right_tail = True
        maxim_x = int(random.random()*7)


dx2 = 0
maxim_x2 = int(random.random()*7)
right_head = True
def head_shake():
    global dx2, maxim_x2, right_head
    if right_head: 
        for i in head_array:
            moveObjectBy(i, 1, 0)
        dx2 += 1    
    else:
        for i in head_array:
            moveObjectBy(i, -1, 0)
        dx2 -= 1
    if right_head and dx2 >= maxim_x2:
        right_head = False
        maxim_x2 = int(random.random()*7)
    elif (not right_head) and dx2 <= -maxim_x2:
        right_head = True
        maxim_x2 = int(random.random()*7)
        


windowSize(600, 800)
canvasSize(600, 800)

flag = False

penColor(136, 236, 255)
brushColor(136, 236, 255)
sky = rectangle(0, 0, 600, 400)  # sky


penColor(68, 255, 74)
brushColor(68, 255, 74)
ground = rectangle(0, 400, 600, 800)  # ground

penColor('yellow')
brushColor('yellow')
coord = generateCoord(50, 600, 350, 0, 0)
creatStars(coord, 0)
tree((128, 64, 28), 'dark green', (217, 0, 40))

mane = [(49, 0, 98), (192, 5, 218), (182, 39, 246)]
mane.extend(((172, 73, 245), (191, 5, 247), (149, 33, 246)))
mane.extend(((143, 0, 255), (205, 1, 203), (152, 18, 150)))
mane.extend(((226, 94, 240), (99, 0, 155)))
tail = [(49, 0, 98), (192, 5, 218), (182, 39, 246)]
tail.extend(((172, 73, 245), (191, 5, 247), (149, 33, 246)))
tail.extend(((143, 0, 255), (205, 1, 203), (152, 18, 150)))
tail.extend(((226, 94, 240), (99, 0, 155)))
axis = generateCoord(10, 17, 9, 10, 8)
unicorn('white', (184, 134, 11), 'white', (184, 134, 11), mane, tail, axis)

onTimer(dayNight, 1000)

onTimer(jump, 1)

onTimer(wind, 30)

onTimer(head_shake, 36)

run()
