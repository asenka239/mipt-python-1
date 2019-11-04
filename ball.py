from tkinter import *
from random import randrange as rnd, choice
import random
import time
import math
from time import sleep

root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='pink')
canv.pack(fill=BOTH,expand=1)

def color_creater():
    color = '#'
    for i in range(0, 6):
        color += choice([str(x) for x in range(0, 10)] +
                      ['a', 'b', 'c', 'd', 'e', 'f'])
    return color

balls = []

def v_creater(side=-1):
    av = 20
    angle = 2 * math.pi * random.random()
    vx = av * math.cos(angle)
    vy = av * math.sin(angle)
    if side == 0:
        vy = +abs(vy)
    if side == 1:
        vx = -abs(vx)
    if side == 2:
        vy = -abs(vy)
    if side == 3:
        vx = +abs(vx)
    return [av * 2 * (random.random() - 0.5), av * 2 * (random.random() - 0.5)]

def new_ball(oldness='old'):
    global balls
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    balls.append({'xy': [x, y], 'v': v_creater(), 'r': r, 'color': color_creater(
    ), 'inside_color': color_creater(), 'oldness': oldness, 'flag': False}) 

class seg:
    def __init__(obj, x, y):
        obj.x = x
        obj.y = y

    def __add__(obj, other):
        return seg(obj.x + other.x, obj.y + other.y)

    def __sub__(obj, other):
        return seg(obj.x - other.x, obj.y - other.y)

    def __truediv__(obj, x):
        return seg(obj.x / x, obj.y / x)

    def __mul__(obj, x):
        return seg(obj.x * x, obj.y * x)

    def sq_abs(obj):
        return obj.x * obj.x + obj.y * obj.y

    def abs(obj):
        return math.sqrt(obj.sq_abs())

    def norm(obj):
        return obj / obj.abs()

def point_mult(a, b):
    return a.x * b.x + a.y * b.y



def update():
    canv.delete(ALL)
    for ball in balls:
        x = ball['xy'][0]
        y = ball['xy'][1]
        r = ball['r']

        if not ball['flag']:
            if x < r:
                ball['v'][0] *= -1
                ball['flag'] = True
            if x > 800 - r:
                ball['v'][0] *= -1
                ball['flag'] = True
            if y < r:
                ball['v'][1] *= -1
                ball['flag'] = True
            if y > 600 - r:
                ball['v'][1] *= -1
                ball['flag'] = True
        else:
            ball['flag'] = False
            if x < r:
                ball['flag'] = True
            if x > 800 - r:
                ball['flag'] = True
            if y < r:
                ball['flag'] = True
            if y > 600 - r:
                ball['flag'] = True
        if ball['oldness'] == 'old':
            canv.create_oval(
                x - r,
                y - r,
                x + r,
                y + r,
                fill=ball['color'],
                width=0)
        else:
            canv.create_oval(
                x - r,
                y - r,
                x + r,
                y + r,
                fill=ball['color'],
                width=0)
            r1 = r / 2.5
            canv.create_oval(
                x - r1,
                y - 0.5*r1,
                x + 2*r1,
                y + r1,
                fill=ball['inside_color'],
                width=0)

        ball['xy'][0] += ball['v'][0] * 0.2
        ball['xy'][1] += ball['v'][1] * 0.2

    for ball in balls:
        for inside_ball in balls:
            diff = seg(inside_ball['xy'][0], inside_ball['xy'][1]) - \
                seg(ball['xy'][0], ball['xy'][1])
            if diff.sq_abs() >= (ball['r'] +
                               inside_ball['r']) ** 2 or diff.sq_abs() == 0:
                continue
            permition = diff.abs() - (ball['r'] + inside_ball['r'])
            norm = diff.norm()
            ball['xy'][0] += (norm * permition / 2).x
            ball['xy'][1] += (norm * permition / 2).y
            inside_ball['xy'][0] -= (norm * permition / 2).x
            inside_ball['xy'][1] -= (norm * permition / 2).y

            v0 = seg(ball['v'][0], ball['v'][1])
            v1 = seg(inside_ball['v'][0], inside_ball['v'][1])
            v0_n = norm * point_mult(v0, norm)
            v1_n = norm * point_mult(v1, norm)
            v0 = v0 - v0_n + v1_n
            v1 = v1 - v1_n + v0_n
            ball['v'][0] = v0.x
            ball['v'][1] = v0.y
            inside_ball['v'][0] = v1.x
            inside_ball['v'][1] = v1.y
    root.after(20, update)



def click(event):
    global count
    hit = [False, False]
    for ball in balls:
        x = ball['xy'][0]
        y = ball['xy'][1]
        r = ball['r']
        suc_hit = (event.x - x) ** 2 + (event.y - y) ** 2 < r ** 2
        if ball['oldness'] == 'old':
            hit[0] = hit[0] or suc_hit
        else:
            hit[1] = hit[1] or suc_hit

    if hit[0]:
        count += 5
    elif hit[1]:
        count += 10
    else:
        count -= 50
    print('Your score now:', count)


for i in range(0, 10):
    new_ball(random.choice(['old', 'new']))


count = 0
update()
canv.bind('<Button-1>', click)
canv.focus_set()
mainloop()