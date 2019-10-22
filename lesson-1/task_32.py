#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_8_18():
    k = 0
    l = 0

    while wall_is_beneath():
        if wall_is_above():
            fill_cell()
        else:
            while not wall_is_above():
                move_up()
                l += 1
                if not cell_is_filled():
                    fill_cell()
                    k += 1
            while not wall_is_beneath():
                move_down()
        move_right()
    t = l - k
    mov('ax', t)


if __name__ == '__main__':
    run_tasks()
