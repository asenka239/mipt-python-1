#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.0005)
def task_4_11():

    move_down()
    move_right()

    for i in range(13):
        k = i
        while k != 13:
            fill_cell()
            k += 1
            move_down()
        move_right()
        for i in range(12 - i):
            move_up()

    for i in range(13):
        move_left()


if __name__ == '__main__':
    run_tasks()

    move_left()
    move_right()
    move_up()
    move_down()
    wall_is_above()
    wall_is_beneath()
    wall_is_on_the_left()
    wall_is_on_the_right()
    fill_cell()
    cell_is_filled()
