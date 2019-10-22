#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.005)
def task_5_10():

    while not wall_is_beneath():

        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        fill_cell()
        if not wall_is_beneath():
            move_down()
        while not wall_is_on_the_left():
            move_left()

    while not wall_is_on_the_right():
        fill_cell()
        move_right()
    fill_cell()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
