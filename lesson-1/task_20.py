#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_3():

    move_down()

    while not wall_is_beneath():
        move_up()
        while not wall_is_on_the_right():
            move_right()
            if not wall_is_on_the_right():
                fill_cell()
            else:
                move_down()
        while not wall_is_on_the_left():
            move_left()
        move_down()     

    move_right()
    move_up()      







if __name__ == '__main__':
    run_tasks()






