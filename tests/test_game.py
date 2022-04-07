from unittest import TestCase
from collections import deque
from model.util import Point, Direction
from model.game import Game
from model.snake import Snake
from model.food import Food

class GameTestCase(TestCase):

    def test_game_init(self):
        """
        Create and test a new Game object.
        """

        game = Game(4, 4)
        assert type(game.snake) == Snake
        assert type(game.food) == Food
        assert game.width == 4
        assert game.height == 4

    def test_update_game(self):
        """
        Test whether the game updates itself properly.
        """

        game = Game(4, 4)
        assert game.snake.get_head_position() == Point(2, 2)
        assert game.snake.direction == Direction.RIGHT
        assert game.food.position == Point(1, 1)

        # Move when there is no user input
        game.update_game(None)
        assert game.snake.get_head_position() == Point(3, 2)
        assert game.snake.direction == Direction.RIGHT
        assert game.food.position == Point(1, 1)

        # Move when there is user input
        game.update_game(Direction.UP)
        assert game.snake.get_head_position() == Point(3, 1)
        assert game.snake.direction == Direction.UP
        assert game.food.position == Point(1, 1)

        # Update when the snake eats food.
        game.update_game(Direction.LEFT)
        game.update_game(None)
        assert game.snake.length == 1
        game.update_game(None) # Snake length and new food position
                                # should be updated here
        assert game.snake.length == 2
        assert game.snake.get_head_position() == Point(0, 1)
        assert game.food.position != Point(1, 1)

        # Reset game when the snake bumps into itself.
        game.snake.positions = deque([
            Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0), Point(3, 1)
        ])
        game.snake.length = 5
        game.snake.direction = Direction.LEFT
        game.food.position = Point(3, 3)
        assert game.snake.get_head_position() == Point(0, 0)
        game.update_game(Direction.DOWN)
        game.update_game(Direction.RIGHT)
        game.update_game(Direction.UP)
        assert game.snake.length == 1
        assert game.snake.get_head_position() == Point(2, 2)
        assert game.food.position == Point(1, 1)

    def test_get_matrix(self):
        """
        Test whether the get_matrix function works properly.
        """

        game = Game(4, 4)
        assert game.food.position == Point(1, 1)
        assert game.snake.get_head_position() == Point(2, 2)
        assert game.snake.length == 1

        assert game.get_matrix() == [
            [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
            [(0, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0)],
            [(0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 0)],
            [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
        ]
