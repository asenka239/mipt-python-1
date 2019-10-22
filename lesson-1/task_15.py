#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_8_21():
    if wall_is_beneath() and wall_is_on_the_left():
        while not wall_is_on_the_right():
            move_right()
        while not wall_is_above():
            move_up()
    elif wall_is_beneath() and wall_is_on_the_right():
        while not wall_is_on_the_left():
            move_left()
        while not wall_is_above():
            move_up()
    elif wall_is_above() and wall_is_on_the_left():
        while not wall_is_on_the_right():
            move_right()
        while not wall_is_beneath():
            move_down()
    elif wall_is_above() and wall_is_on_the_right():
        while not wall_is_on_the_left():
            move_left()
        while not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()
