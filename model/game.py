import pygame
import snake
import food
from util import Direction

# initialize speed
speed = 2
clock = pygame.time.Clock()

# Window size
window_x = 8
window_y = 8

# defining colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
red = pygame.Color(255, 0, 0)


def game_over():
    pygame.display.flip()
    pygame.quit()
    quit()


# Main Function
# Initialising pygame
pygame.init()

# Initialise game window
window = pygame.display.set_mode((window_x*100, window_y*100))

snake = snake.Snake(window_x, window_y)
food = food.Food(window_x, window_y)

is_running = True

while is_running:

    snake_head = snake.get_head_position()

    if snake_head.x >= window_x or snake_head.x <= 0: 
        game_over()
    elif snake_head.y >= window_y or snake_head.y <= 0:
        game_over()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.turn(Direction.UP)
            if event.key == pygame.K_DOWN:
                snake.turn(Direction.DOWN)
            if event.key == pygame.K_LEFT:
                snake.turn(Direction.LEFT)
            if event.key == pygame.K_RIGHT:
                snake.turn(Direction.RIGHT)
            if event.key == pygame.K_1:
                is_running = False

    collision = snake.get_head_position() == food.position
    grow = False

    if collision:
        grow = True
        food.move_random_position(snake_pos=snake.positions)

    snake.move(grow=grow)

    window.fill(black)

    pygame.draw.rect(
        window, red, pygame.Rect(
            food.position.x*100, food.position.y*100, 100, 100))

    for curr in snake.positions:
        pygame.draw.rect(
            window, green, pygame.Rect(
                curr.x*100, curr.y*100, 100, 100))

    # clock ticker
    pygame.display.update()
    clock.tick(speed)
