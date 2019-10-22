#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.0002)
def task_2_4():
    def func():
        move_right()
        fill_cell()
        move_down()
        fill_cell()
        move_down()
        fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_right()
        move_right()
        fill_cell()
        move_left()
        move_left()
        move_up()

    for i in range(4):
        func()
        for j in range(9):
            move_right()
            move_right()
            move_right()
            move_right()
            func()
        for j in range(36):
            move_left()
        for j in range(4):
            move_down()
    func()
    for k in range(9):
        move_right()
        move_right()
        move_right()
        move_right()
        func()
    for k in range(36):
        move_left()


if __name__ == '__main__':
    run_tasks()
