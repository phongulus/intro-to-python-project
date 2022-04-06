import model.snake as snake_
import model.food as food_
from model.util import Direction
from time import time
from send_unicorn import send_matrix_data
import controls

# initialize speed
speed = 5

# Window size
window_x = 8
window_y = 8

# defining colors
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

def get_blank_matrix():
    mat = [0] * 8
    for y in range(8):
        row = []
        for x in range(8):
            row.append(black)
        mat[y] = row
    return mat

# def game_over():
#     pygame.display.flip()
#     pygame.quit()
#     quit()


# Main Function

snake = snake_.Snake(window_x, window_y)
food = food_.Food(window_x, window_y)
is_running = True
cur_time = time()
last_event = None

while is_running:
    
    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_UP:
    #             snake.turn(Direction.UP)
    #         if event.key == pygame.K_DOWN:
    #             snake.turn(Direction.DOWN)
    #         if event.key == pygame.K_LEFT:
    #             snake.turn(Direction.LEFT)
    #         if event.key == pygame.K_RIGHT:
    #             snake.turn(Direction.RIGHT)
    #         if event.key == pygame.K_1:
    #             is_running = False

    if controls.is_up_pressed():
        last_event = Direction.UP

    if controls.is_down_pressed():
        last_event = Direction.DOWN

    if controls.is_left_pressed():
        last_event = Direction.LEFT

    if controls.is_right_pressed():
        last_event = Direction.RIGHT

    if cur_time + speed >= time():

        snake_head = snake.get_head_position()

        # Reset the game if snake is outside of window
        if (snake_head.x >= window_x or snake_head.x <= 0 or
            snake_head.y >= window_y or snake_head.y <= 0): 
            snake = snake_.Snake(window_x, window_y)
            food = food_.Food(window_x, window_y)

        if last_event:
            snake.turn(last_event)

        collision = snake.get_head_position() == food.position
        grow = False

        if collision:
            grow = True
            food.move_random_position(snake_pos=snake.positions)

        snake.move(grow=grow)

        mat = get_blank_matrix()
        mat[food.position.y][food.position.x] = red
        for curr in snake.positions:
            if 0 <= curr.y and curr.y <= 7 and 0 <= curr.x and curr.x <= 7:
                mat[curr.y][curr.x] = green

        send_matrix_data(mat)

        cur_time = time()
        last_event = None
