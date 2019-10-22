#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_9_3():
    k = 1

    while not wall_is_on_the_right():
        move_right()
        k += 1
    while not wall_is_on_the_left():
        move_left()

    x = 1
    y = 1

    for i in range(k - 1):
        for j in range(k):
            if x != i + 1 and y != j + 1 and x + y != k + 1:
                fill_cell()
            if not wall_is_on_the_right():
                move_right()
                x += 1
        for l in range(k - 1):
            move_left()
            x -= 1
        move_down()
        y += 1

    for j in range(k - 2):
        move_right()
        fill_cell()
    for l in range(k - 2):
        move_left()


if __name__ == '__main__':
    run_tasks()
