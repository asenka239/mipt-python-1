#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    k = 0
    while not wall_is_on_the_right() and k < 3:
        move_right()
        if cell_is_filled():
            k += 1
        else:
            k = 0


if __name__ == '__main__':
    run_tasks()
