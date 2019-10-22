#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.0001)
def task_8_30():

    flag = 0

    while flag != 1:
        flag = 0
        while not wall_is_on_the_right() and wall_is_beneath():
            move_right()
        while not wall_is_on_the_left() and wall_is_beneath():
            move_left()
        if wall_is_on_the_left() and wall_is_beneath():
            flag = 1
        else:
            while not wall_is_beneath():
                move_down()


if __name__ == '__main__':
    run_tasks()
