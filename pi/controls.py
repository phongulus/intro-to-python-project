import board
import busio
from digitalio import DigitalInOut, Direction, Pull

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT
button_A.pull = Pull.UP

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT
button_B.pull = Pull.UP

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT
button_L.pull = Pull.UP

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT
button_R.pull = Pull.UP

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT
button_U.pull = Pull.UP

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT
button_D.pull = Pull.UP

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT
button_C.pull = Pull.UP

def is_up_pressed():
    if button_U.value:
        return False
    return True

def is_down_pressed():
    if button_D.value:
        return False
    return True

def is_left_pressed():
    if button_L.value:
        return False
    return True

def is_right_pressed():
    if button_R.value:
        return False
    return True

def is_center_pressed():
    if button_C.value:
        return False
    return True

def is_A_pressed():
    if button_A.value:
        return False
    return True

def is_B_pressed():
    if button_B.value:
        return False
    return True
