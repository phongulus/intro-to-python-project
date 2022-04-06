import model.snake as snake_
import model.food as food_
from model.util import Direction, Color
from time import sleep, time
from send_unicorn import send_matrix_data
import controls

# initialize speed
SPEED = 0.6

# Window size
WIDTH = 8
HEIGHT = 8

# defining colors
BLANK = Color(0, 0, 0)

def reset_matrix():
    matrix = [0] * 8
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            row.append(BLANK)
        matrix[y] = row
    return matrix


# Main Function

snake = snake_.Snake(WIDTH, HEIGHT)
food = food_.Food(WIDTH, HEIGHT)

is_running = True
cur_time = time()
last_event = None

while is_running:
    
    if controls.is_up_pressed():
        last_event = Direction.UP

    if controls.is_down_pressed():
        last_event = Direction.DOWN

    if controls.is_left_pressed():
        last_event = Direction.LEFT

    if controls.is_right_pressed():
        last_event = Direction.RIGHT

    if cur_time + SPEED <= time():

        snake_head = snake.get_head_position()

        if last_event:
            snake.turn(last_event)

        grow = snake.get_head_position() == food.position

        if grow:
            food.move_random_position(snake_pos=snake.positions)

        if not snake.move(grow=grow):
            snake.reset()
            food.reset()

        mat = reset_matrix()
        mat[food.position.y][food.position.x] = food.color
        for curr in snake.positions:
                mat[curr.y][curr.x] = snake.color

        send_matrix_data(mat)

        cur_time = time()
        last_event = None
