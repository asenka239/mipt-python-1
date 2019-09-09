#!/usr/bin/python3

from pyrob.api import *


@task(delay = 0.01)
def task_8_27():
    
    while not cell_is_filled():
        move_up()

    move_left()

    if not cell_is_filled():
        move_right()
        move_right()


if __name__ == '__main__':
    run_tasks()

