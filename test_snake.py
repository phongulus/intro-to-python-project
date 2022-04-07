from unittest import TestCase
from model.snake import Snake
from model.util import Point, Direction
from collections import deque


class SnakeTestCase(TestCase):

    def test_snake_init(self):
        s = Snake(width=8, height=8)
        assert type(s) == Snake
        assert s.screen_width == 8
        assert s.screen_height == 8

        assert s.positions[0] == Point(4, 4)
        assert s.color is not None
        assert s.direction is not None
        assert s.length == 1

    def test_get_head_position(self):
        s = Snake(width=8, height=8)
        test_snake = deque([Point(1, 1), Point(1, 2), Point(1, 3)])

        s.positions = test_snake
        assert s.get_head_position() == test_snake[0]

    def test_turn_short(self):
        s = Snake(width=8, height=8)
        s.length = 1
        s.direction = Direction.RIGHT

        s.turn(Direction.UP)
        assert s.direction == Direction.UP
        s.turn(Direction.DOWN)
        assert s.direction == Direction.DOWN

        s.turn(Direction.LEFT)
        assert s.direction == Direction.LEFT
        s.turn(Direction.RIGHT)
        assert s.direction == Direction.RIGHT

        s.turn(Direction.DOWN)
        assert s.direction == Direction.DOWN
        s.turn(Direction.UP)
        assert s.direction == Direction.UP

        s.turn(Direction.RIGHT)
        assert s.direction == Direction.RIGHT
        s.turn(Direction.LEFT)
        assert s.direction == Direction.LEFT

    def test_turn_long(self):
        s = Snake(width=8, height=8)
        s.length = 2
        s.direction = Direction.RIGHT

        s.turn(Direction.UP)
        assert s.direction == Direction.UP
        s.turn(Direction.DOWN)
        assert s.direction == Direction.UP

        s.turn(Direction.LEFT)
        assert s.direction == Direction.LEFT
        s.turn(Direction.RIGHT)
        assert s.direction == Direction.LEFT

        s.turn(Direction.DOWN)
        assert s.direction == Direction.DOWN
        s.turn(Direction.UP)
        assert s.direction == Direction.DOWN

        s.turn(Direction.RIGHT)
        assert s.direction == Direction.RIGHT
        s.turn(Direction.LEFT)
        assert s.direction == Direction.RIGHT

    def test_move(self):
        s = Snake(width=8, height=8)
        s.length = 1
        s.direction = Direction.RIGHT
        s.positions = deque([Point(4, 4)])

        prev_head = s.get_head_position()
        s.move()
        assert s.length == 1
        assert s.get_head_position() == prev_head + Direction.RIGHT.value

        s.move(grow=True)
        assert s.length == 2

        s.direction = Direction.UP
        prev_head = s.get_head_position()
        s.move()
        assert s.length == len(s.positions)
        assert s.get_head_position() == prev_head + Direction.UP.value

    def test_rest(self):
        s = Snake(8, 8)
        s.length = 12
        s.direction = Direction.DOWN
        test_snake = deque([Point(1, 1), Point(1, 2), Point(1, 3)])
        s.positions = test_snake

        new_s = Snake(8, 8)

        s.reset()
        assert s.length == new_s.length
        assert s.direction == new_s.direction
        assert s.positions == new_s.positions
