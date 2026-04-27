"""
File: Steeplechase.py
Name: 劉家佑
---------------------------------
劉家佑:
"""

from karel.stanfordkarel import *
def main():
    for i in range(7):
        #wall or not?
        while front_is_clear():
            move()
        #cross a wall
        jump()


    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
def turn_right():
    for i in range(3):
        turn_left()
def jump():
    up()
    move()
    down()
def up():
    while not front_is_clear():
        #east
        turn_left()
        move()
        #north
        turn_right()
        #east
def down():
    turn_right()
    #east
    move()
    #south
    while front_is_clear():
        move()
    turn_left()
    #east



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
