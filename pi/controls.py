import board
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
    """
    Checking if the 'up' button is pressed.

    Parameters:
    ----
    None

    Return:
    ----
    `<Boolean>`: Returns True if the 'up' button is pressed and if not False.
    """
    if button_U.value:
        return False
    return True


def is_down_pressed():
    """
    Checking if the 'down' button is pressed.

    Parameters:
    ----
    None

    Return:
    ----
    `<Boolean>`: Returns True if the 'down' button is pressed and if not False.
    """
    if button_D.value:
        return False
    return True


def is_left_pressed():
    """
    Checking if the 'left' button is pressed.

    Parameters:
    ----
    None

    Return:
    ----
    `<Boolean>`: Returns True if the 'left' button is pressed and if not False.
    """
    if button_L.value:
        return False
    return True


def is_right_pressed():
    """
    Checking if the 'right' button is pressed.

    Parameters:
    ----
    None

    Return:
    ----
    `<Boolean>`: Returns True if the 'right' button is pressed and
    if not False.
    """
    if button_R.value:
        return False
    return True


def is_center_pressed():
    """
    Checking if the 'center' button is pressed.

    Parameters:
    ----
    None

    Return:
    ----
    `<Boolean>`: Returns True if the 'center' button is pressed and
    if not False.
    """
    if button_C.value:
        return False
    return True


def is_A_pressed():
    """
    Checking if the button 'A' is pressed.

    Parameters:
    ----
    None

    Return:
    ----
    `<Boolean>`: Returns True if the button 'A' is pressed and if not False.
    """
    if button_A.value:
        return False
    return True


def is_B_pressed():
    """
    Checking if the button 'B' is pressed.

    Parameters:
    ----
    None

    Return:
    ----
    `<Boolean>`: Returns True if the button 'B' is pressed and if not False.
    """
    if button_B.value:
        return False
    return True
