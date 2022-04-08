from unittest import TestCase
from model.snake import Snake
from model.util import Point, Direction
from collections import deque


class SnakeTestCase(TestCase):

    def test_snake_init(self):
        """
        Initialize a new Snake object and test its default attributes.
        """

        s = Snake(width=8, height=8)
        assert type(s) == Snake
        assert s.screen_width == 8
        assert s.screen_height == 8

        assert s.positions[0] == Point(4, 4)
        assert len(s.positions) == 1
        assert s.length == 1

        assert s.color is not None
        assert s.direction is not None

    def test_get_head_position(self):
        """
        Check that the get_head_position function correctly returns
        the position of the Snake's head.
        """

        s = Snake(width=8, height=8)
        test_snake = deque([Point(1, 1), Point(1, 2), Point(1, 3)])

        s.positions = test_snake
        assert type(s.get_head_position()) == Point
        assert s.get_head_position() == test_snake[0]

    def test_turn_short(self):
        """
        Initialize a new Snake object and test its turning behavior (i.e.
        when it changes its movement direction), especially when turning
        in the opposite of the current direction. This should be possible
        when the length of the snake is 1.
        """

        # Initialise the Snake and verify some important defaults.
        s = Snake(width=8, height=8)
        assert s.length == 1
        assert s.direction == Direction.RIGHT

        # Check if the Snake of length 1 can turn up and down repeatedly.
        s.turn(Direction.UP)
        assert s.direction == Direction.UP
        s.turn(Direction.DOWN)
        assert s.direction == Direction.DOWN
        s.turn(Direction.UP)
        assert s.direction == Direction.UP

        # Check if the Snake of length 1 can turn left and right repeatedly.
        s.turn(Direction.LEFT)
        assert s.direction == Direction.LEFT
        s.turn(Direction.RIGHT)
        assert s.direction == Direction.RIGHT
        s.turn(Direction.LEFT)
        assert s.direction == Direction.LEFT

    def test_turn_long(self):
        """
        Initialize a new Snake object and test its turning behavior (i.e.
        when it changes its movement direction), especially when turning
        in the opposite of the current direction. This should not be possible
        when the length of the snake is 2 or longer.
        """

        s = Snake(width=8, height=8)
        s.move(grow=True)
        assert s.length == 2
        assert s.direction == Direction.RIGHT

        # We verify that the Snake of length 2 cannot turn in
        # opposite directions (up and down in this case). We
        # then check its turning in non-opposite directions, then
        # rinse and repeat.
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
        """
        Initialize a Snake object and check if it moves as expected.
        """

        # Initialise the Snake and verify some important defaults.
        s = Snake(width=6, height=6)
        assert s.length == 1
        assert s.direction == Direction.RIGHT
        assert s.positions[0] == Point(3, 3)

        # Simple move to the right. Note that s.move() should return True
        # when the move is valid (i.e. the snake does not bump into itself.)
        assert s.move()
        assert s.length == 1
        assert s.get_head_position() == Point(4, 3)

        # Move when growing (i.e. after eating a fruit).
        assert s.move(grow=True)
        assert s.length == 2
        assert s.get_head_position() == Point(5, 3)

        # Move outside of right screen boundary.
        assert s.move()
        assert s.length == 2
        assert s.get_head_position() == Point(0, 3)
        assert s.positions[1] == Point(5, 3)

        # Move after turning.
        s.direction = Direction.UP
        assert s.move()
        assert s.get_head_position() == Point(0, 2)
        assert s.positions[1] == Point(0, 3)

        # Move outside of upper screen boundary
        assert s.move()
        assert s.move()
        assert s.move()
        assert s.get_head_position() == Point(0, 5)
        assert s.positions[1] == Point(0, 0)

        # Move outside of left screen boundary
        s.direction = Direction.LEFT
        assert s.move()
        assert s.get_head_position() == Point(5, 5)
        assert s.positions[1] == Point(0, 5)

        # Move outside of lower screen boundary
        s.direction = Direction.DOWN
        assert s.move()
        assert s.get_head_position() == Point(5, 0)
        assert s.positions[1] == Point(5, 5)

        # Check for invalid move
        assert s.move(grow=True)
        assert s.move(grow=True)
        assert s.move(grow=True)
        s.direction = Direction.LEFT
        assert s.move()
        s.direction = Direction.UP
        assert s.move()
        s.direction = Direction.RIGHT
        assert not s.move()

    def test_reset(self):
        """
        Check that the reset function correctly resets the Snake length,
        position and direction to default values.
        """

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
