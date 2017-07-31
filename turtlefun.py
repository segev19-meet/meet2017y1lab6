UP_ARROW="UP"
LEFT_ARROW="LEFT"
DOWN_ARROW="DOWN"
RIGHT_ARROW="RIGHT"
SPACEBAR="SPACE"

UP=0
DOWN=1
LEFT=2
RIGHT=3
DIRECTION=UP


def up():
    global direction
    direction=UP
    print("you pressed UP")
    


def left():
    global direction
    direction=LEFT
    print("you pressed LEFT")



def right():
    global direction
    direction=RIGHT
    print("you pressed RIGHT")
