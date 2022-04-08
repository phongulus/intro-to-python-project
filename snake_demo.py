from model.util import Direction
from model.game import Game
from time import time
from send_unicorn import send_matrix_data
import controls

# Initialize speed
SPEED = 0.6

# Window size
WIDTH = 8
HEIGHT = 8

# Instantiate a Game instance.
game = Game(WIDTH, HEIGHT)

# Initialize variables to keep track of time and user input.
cur_time = time()
last_event = None

# Main loop
while True:
    
    # Even when the game is waiting for the next frame,
    # take and remember inputs from the player.
    if controls.is_up_pressed():
        last_event = Direction.UP
    if controls.is_down_pressed():
        last_event = Direction.DOWN
    if controls.is_left_pressed():
        last_event = Direction.LEFT
    if controls.is_right_pressed():
        last_event = Direction.RIGHT

    if cur_time + SPEED <= time():
        game.update_game(last_event)
        send_matrix_data(game.get_matrix())
        cur_time = time()
        last_event = None
